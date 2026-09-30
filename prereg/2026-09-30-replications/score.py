"""Frozen, offline analysis for R1. No model imports, network, or run capability.

Input is one JSON object with `records` and `recall` lists. Records have study,
arm (a/b), person_id, index (0..39), value (0/1 or null), and status
(observed/voluntary_exit/technical_failure/not_run). A portfolio supplies two
records with the same person_id/index, arm a = cell_0, b = cell_1.
Recall entries have study and status (positive/negative/unknown).
The future runner must also retain raw traces; this file never manufactures them.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

TARGET = 40
Z = 1.959963984540054
Z_PAIRED = 2.241402727604947  # Two 97.5% intervals: Bonferroni coverage target 95%.


def wilson(x: int, n: int, z: float = Z) -> list[float] | None:
    if not n:
        return None
    p = x / n
    den = 1 + z * z / n
    center = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [max(0, center - half), min(1, center + half)]


def newcombe(a: dict, b: dict) -> list[float]:
    pa, pb = a['x'] / a['n'], b['x'] / b['n']
    la, ua = wilson(a['x'], a['n'])
    lb, ub = wilson(b['x'], b['n'])
    return [max(-1, pb - pa - math.hypot(pb - lb, ua - pa)),
            min(1, pb - pa + math.hypot(ub - pb, pa - la))]


def paired_interval(cells: dict) -> list[float]:
    # The paired difference is P(A=0,B=1) - P(A=1,B=0). Simultaneous
    # score intervals remain nondegenerate even with no observed discordance.
    n = sum(cells.values())
    low01, high01 = wilson(cells['01'], n, Z_PAIRED)
    low10, high10 = wilson(cells['10'], n, Z_PAIRED)
    return [low01 - high10, high01 - low10]


def rate(arm: dict) -> float:
    return arm['x'] / arm['n'] if arm.get('n') else arm['rate']


def score(data: dict, truth: dict) -> dict:
    rows = data['records']
    valid_ids = {item['id'] for item in truth['studies']}
    seen = set()
    people = set()
    for row in rows:
        key = (row['study'], row['arm'], row['index'])
        if row['study'] not in valid_ids or row['arm'] not in ('a', 'b') or type(row['index']) is not int or not 0 <= row['index'] < TARGET:
            raise ValueError(f'Unknown study/arm/index: {key}')
        if key in seen:
            raise ValueError(f'Duplicate scheduled slot: {key}')
        seen.add(key)
        if not isinstance(row['person_id'], str) or not row['person_id'].strip():
            raise ValueError('Every scheduled slot needs its frozen panel persona ID')
        person_key = (row['study'], row['arm'], row['person_id'])
        if person_key in people:
            raise ValueError(f'Repeated person within condition: {person_key}')
        people.add(person_key)
        if row['status'] not in ('observed', 'voluntary_exit', 'technical_failure', 'not_run'):
            raise ValueError('Unknown session status')
        if row['status'] == 'observed' and (type(row['value']) is not int or row['value'] not in (0, 1)):
            raise ValueError('Observed outcomes must be binary integers')
        if row['status'] == 'voluntary_exit' and row.get('value') not in (0, None):
            raise ValueError('Exit without a decision is not a positive choice')
        if row['status'] in ('technical_failure', 'not_run') and row.get('value') is not None:
            raise ValueError('Unknown outcomes must remain null')
    recalls = {}
    for item in data.get('recall', []):
        if item['study'] not in valid_ids or item['study'] in recalls or item['status'] not in ('positive', 'negative', 'unknown'):
            raise ValueError('Invalid or duplicate recall classification')
        recalls[item['study']] = item['status']
    output = []
    for study in truth['studies']:
        arms = {}
        selected = {}
        for arm in ('a', 'b'):
            selected[arm] = [r for r in rows if r['study'] == study['id'] and r['arm'] == arm]
            observed = [r for r in selected[arm] if r['status'] in ('observed', 'voluntary_exit')]
            x = sum(r['value'] or 0 for r in observed)
            arms[arm] = {'x': x, 'n': len(observed), 'scheduled': TARGET,
                         'unknown': TARGET - len(observed), 'rate': x / len(observed) if observed else None,
                         'ci95': wilson(x, len(observed))}
        full = all(arm['unknown'] == 0 for arm in arms.values())
        hd = rate(study['b']) - rate(study['a'])
        hc = paired_interval(study['human_paired']) if 'human_paired' in study else (
            newcombe(study['a'], study['b']) if study['a'].get('n') and study['b'].get('n') else None)
        # Unknown outcomes are bounded, never imputed as a refusal.
        bounds = [(arms['b']['x'] - arms['a']['x'] - arms['a']['unknown']) / TARGET,
                  (arms['b']['x'] + arms['b']['unknown'] - arms['a']['x']) / TARGET]
        sd = sc = error = match = None
        if full:
            if study['id'] == 'R07':
                aa = {r['index']: r for r in selected['a']}
                bb = {r['index']: r for r in selected['b']}
                cells = {key: 0 for key in ('00', '01', '10', '11')}
                for idx, row in aa.items():
                    if row['person_id'] != bb[idx]['person_id']:
                        raise ValueError('R07 requires the same person in each pair')
                    cells[f"{row['value'] or 0}{bb[idx]['value'] or 0}"] += 1
                sc = paired_interval(cells)
            else:
                if {r['person_id'] for r in selected['a']} & {r['person_id'] for r in selected['b']}:
                    raise ValueError('Between-person studies require disjoint arms')
                sc = newcombe(arms['a'], arms['b'])
            sd = arms['b']['rate'] - arms['a']['rate']
            error = sd - hd
            match = int(sd * hd > 0)  # Exact ties count zero, never half a success.
        output.append({'study': study['id'], 'group': study['group'], 'fame': study['fame'],
                       'recall': recalls.get(study['id'], 'unknown'), 'human': study,
                       'human_delta': hd, 'human_delta_ci95': hc,
                       'human_rounding_half_width': study.get('rounding_half_width', 0),
                       'simulation': arms, 'complete': full, 'sim_delta': sd, 'sim_delta_ci95': sc,
                       'missing_outcome_delta_bounds': bounds, 'direction_match': match,
                       'signed_error': error, 'absolute_error': abs(error) if error is not None else None,
                       'error_ci95_conditional_on_human_point': [x - hd for x in sc] if sc else None})
    complete = all(x['complete'] for x in output)
    recalls_complete = all(x['recall'] != 'unknown' for x in output)
    successes = sum(x['direction_match'] or 0 for x in output)
    groups = {}
    for group in sorted({x['group'] for x in output}):
        members = [x for x in output if x['group'] == group]
        groups[group] = sum(x['direction_match'] for x in members) / len(members) if all(x['complete'] for x in members) else None
    splits = {}
    for field, labels in [('fame', ['high', 'lower']), ('recall', ['positive', 'negative', 'unknown'])]:
        for label in labels:
            subset = [x for x in output if x[field] == label]
            finished = [x for x in subset if x['complete']]
            splits[f'{field}:{label}'] = {'registered': len(subset), 'completed': len(finished),
                                         'matches': sum(x['direction_match'] for x in finished)}
    negative = [x for x in output if x['recall'] == 'negative']
    recall_survival = 'UNASSESSABLE'
    if complete and recalls_complete and len(negative) >= 3:
        negative_share = sum(x['direction_match'] for x in negative) / len(negative)
        recall_survival = 'PASS' if negative_share >= successes / len(output) - .15 else 'FAIL'
    return {'studies': output, 'registered_studies': len(output), 'complete': complete,
            'recall_complete': recalls_complete,
            'verdict': ('PASS' if successes >= 7 else 'FAIL') if complete and recalls_complete else 'INCOMPLETE',
            'direction_matches': successes, 'direction_share': successes / len(output) if complete else None,
            'descriptive_wilson_ci95': wilson(successes, len(output)) if complete else None,
            'coin_tail_probability_descriptive': sum(math.comb(8, k) for k in range(successes, 9)) / 256 if complete else None,
            'source_group_shares': groups,
            'source_group_equal_weight_mean': sum(groups.values()) / len(groups) if complete else None,
            'splits': splits,
            'absolute_delta_error_mean': sum(x['absolute_error'] for x in output) / len(output) if complete else None,
            'within_10pp': sum(x['absolute_error'] <= .10 for x in output) if complete else None,
            'recall_survival_secondary': recall_survival,
            'limitations': ['Eight purposively chosen experiments in five source groups; binomial interval is descriptive.',
                            'Human field cell denominators unavailable for R03-R05; no fabricated human intervals.',
                            'Error intervals condition on the human point estimate, not joint human/simulation uncertainty.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('observations', type=Path)
    args = parser.parse_args()
    human = json.loads(Path(__file__).with_name('human.json').read_text())
    print(json.dumps(score(json.loads(args.observations.read_text()), human), indent=2))
