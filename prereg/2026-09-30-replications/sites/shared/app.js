/* Local stimuli only. No services, analytics, model clients, or source outcomes. */
(() => {
  'use strict';
  const site = document.body.dataset.site;
  const query = new URLSearchParams(location.search);
  const variant = query.get('v');
  const serial = query.get('i');
  if (!/^s0[1-8]$/.test(site ?? '') || !['a', 'b'].includes(variant) || !/^(0|[1-9]\d?)$/.test(serial) || Number(serial) > 39) {
    document.body.innerHTML = '<main class="invalid"><h1>This address is incomplete</h1><p>Open the supplied page address, including its version and visit number.</p></main>';
    return;
  }
  const index = Number(serial);
  const isB = variant === 'b';
  const root = document.getElementById('app');
  const storageKey = `visit:${site}:${variant}:${index}`;
  const state = { schema: 1, site, variant, index, events: [], decisions: {}, terminal: false };
  // A fresh browser context is required for every visit. Reloads keep the first choices.
  try {
    const previous = JSON.parse(sessionStorage.getItem(storageKey) ?? 'null');
    if (previous?.schema === 1) {
      Object.assign(state.decisions, previous.decisions);
      state.events.push(...previous.events);
      state.terminal = previous.terminal;
    }
  } catch { /* The in-memory trace also works with storage disabled. */ }
  const started = performance.now();
  function emit(type, detail = {}) {
    state.events.push({ type, elapsed_ms: Math.round(performance.now() - started), ...detail });
    try { sessionStorage.setItem(storageKey, JSON.stringify(state)); } catch { /* Optional persistence. */ }
    window.dispatchEvent(new CustomEvent('replication-event', { detail: { type, ...detail } }));
  }
  function decide(key, value, choice) {
    if (Object.hasOwn(state.decisions, key)) return;
    state.decisions[key] = { value, choice };
    document.body.dataset.choice = choice;
    emit('decision', { key, value, choice });
  }
  // A later harness may read this after the browser session; it does not alter behavior.
  window.replicationExport = () => JSON.parse(JSON.stringify(state));
  function terminal(message) {
    state.terminal = true;
    emit('terminal');
    root.innerHTML = `<section class="sheet"><h1>Thank you</h1><p>${message}</p></section>`;
  }
  function masthead(brand, section) {
    return `<header class="masthead"><strong>${brand}</strong><span>${section}</span></header>`;
  }
  function choices(options, selected = null, name = 'answer') {
    return `<div class="choices">${options.map(([value, text]) => `<label><input type="radio" name="${name}" value="${value}" ${selected === value ? 'checked' : ''} required><span>${text}</span></label>`).join('')}</div>`;
  }
  function formPage(title, intro, options, selected, onSubmit, extra = '', brand = 'Harbor Research') {
    root.innerHTML = `${masthead(brand, 'Member questionnaire')}<section class="sheet"><div class="eyebrow">Your preferences</div><h1>${title}</h1>${intro}<form>${choices(options, selected)}${extra}<div class="actions"><button class="primary" type="submit">Continue</button></div></form></section>`;
    root.querySelector('form').addEventListener('submit', event => {
      event.preventDefault();
      const data = new FormData(event.currentTarget);
      onSubmit(String(data.get('answer')), data);
    });
  }
  function subscription() {
    const isSecond = site === 's02';
    const price = isSecond ? (index % 2 ? '38.99' : '8.99') : (index % 2 ? '8.99' : '2.99');
    const months = isSecond ? 'one month' : 'six months';
    // All form backgrounds occur in each R02 content arm, in a fixed 40-visit block.
    const slot = Math.floor(index / 2);
    const background = slot < 7 ? 'plain' : slot < 11 ? 'recommended' : slot < 16 ? 'default' : 'options';
    const mild = !isSecond && isB;
    const useOptions = mild || (isSecond && background === 'options');
    const useDefault = mild || (isSecond && background === 'default');
    const recommend = mild || (isSecond && background === 'recommended');
    const renewal = `After ${months}, SecureNest Account Watch renews at $${price} each month. You may cancel whenever you wish.`;
    const intro = `<p>Your questionnaire responses indicate that protecting your online accounts matters to you. Using the location details supplied earlier, our system has identified your postal address.</p><p>Our partner, SecureNest, provides account-exposure alerts and identity monitoring. Your questionnaire answers will be shared with the partner. You have been enrolled for ${months} without charge${isSecond && isB ? '*; terms apply.' : '.'}</p>${isSecond && isB ? '' : `<p class="renewal">${renewal}</p>`}`;
    formPage('Your account protection offer', intro,
      [['yes', recommend ? 'Keep the plan and proceed (suggested)' : 'Keep the plan'], ['no', useOptions ? 'See my alternatives' : 'Decline the plan']],
      useDefault ? 'yes' : null,
      value => {
        if (isSecond) {
          decide('primary', value === 'yes' ? 1 : 0, value === 'yes' ? 'enroll' : useOptions ? 'alternatives' : 'decline');
          terminal('Your initial selection has been saved.');
        } else if (value === 'yes') {
          decide('primary', 1, 'enroll'); terminal('Your plan selection has been saved.');
        } else if (!mild) {
          decide('primary', 0, 'decline'); terminal('Your plan selection has been saved.');
        } else {
          emit('alternatives');
          formPage('Review your alternatives', '<p>Please choose how you want to proceed.</p>',
            [['no', 'I am willing to leave my accounts and identity without this protection.'], ['yes', 'After considering the alternatives, I want account alerts and identity monitoring.']], null,
            answer => {
              if (answer === 'yes') { decide('primary', 1, 'enroll'); terminal('Your plan selection has been saved.'); }
              else reasons();
            });
        }
      }, isSecond && isB ? `<p class="renewal muted">* ${renewal}</p>` : '');
    function reasons() {
      emit('reasons');
      formPage('Why leave your accounts unprotected?', '<p>Select the reason that best describes your decision.</p>',
        [['damaged', 'My account reputation is already poor.'], ['unlikely', 'Even though many households face identity fraud, I do not think it could affect mine.'], ['covered', 'I already pay for account and identity monitoring.'], ['nothing', 'I have nothing private that someone could misuse.'], ['other', 'Another reason (please explain below).'], ['yes', 'I have reconsidered: keep my free monitoring plan.']], null,
        (answer, data) => {
          if (answer === 'other' && !String(data.get('reason') ?? '').trim()) {
            const field = root.querySelector('textarea'); field.setCustomValidity('Please give your reason.'); field.reportValidity(); return;
          }
          decide('primary', answer === 'yes' ? 1 : 0, answer === 'yes' ? 'enroll' : 'decline');
          terminal('Your plan selection has been saved.');
        }, '<label for="reason">Your reason</label><textarea id="reason" name="reason"></textarea>');
      root.querySelector('textarea').addEventListener('input', event => event.target.setCustomValidity(''));
      root.querySelectorAll('input[name="answer"]').forEach(input => input.addEventListener('change', () => root.querySelector('textarea').setCustomValidity('')));
    }
  }
  function article() {
    root.innerHTML = `${masthead('Werkblick', 'Unabhängige Produktinformationen')}<main class="article-layout"><article class="article"><p class="eyebrow">Unterwegs · Kaufberatung</p><h1>Eine kompakte Leuchte für lange Abende draußen</h1><p>Die neue Uferlicht Mini passt in kleine Taschen. Wir erklären, wie lange sie leuchtet und welche Ausstattung sich im Alltag bewährt.</p><div class="illustration" aria-label="Illustration einer tragbaren Leuchte" role="img"><div class="product-shape"></div></div><h2 id="laufzeit">Laufzeit und Laden</h2><p>Bei mittlerer Helligkeit hält der Akku bis zu acht Stunden. Ein vollständiger Ladevorgang dauert etwa drei Stunden. Das Kabel gehört zum Lieferumfang.</p><h2 id="details">Was steckt im Gehäuse?</h2><p>Ein Tragebügel, drei Helligkeitsstufen und ein spritzwassergeschütztes Gehäuse machen die Leuchte vielseitig. Für Dauerregen ist sie nicht ausgelegt.</p><h2>Für wen lohnt sie sich?</h2><p>Wer Licht für Balkon oder kurze Ausflüge sucht, bekommt ein einfaches Gerät. Für mehrtägige Touren sollte eine zusätzliche Stromquelle eingeplant werden.</p></article><aside class="sidebar"><h2>In diesem Artikel</h2><ul><li><a href="#laufzeit">Akku und Laufzeit</a></li><li><a href="#details">Ausstattung</a></li></ul><p>Weitere Ratgeber zu kleinen Geräten und Zubehör.</p></aside></main>`;
  }
  function purposes(checked, fixed = true) {
    const optional = [['design', 'Darstellung und Personalisierung'], ['analytics', 'Nutzungsstatistik'], ['social', 'Soziale Inhalte'], ['marketing', 'Werbung']];
    const order = index % optional.length;
    const rows = [...optional.slice(order), ...optional.slice(0, order)];
    return `${fixed ? '<label><input type="checkbox" checked disabled>Technisch erforderlich</label>' : ''}${rows.map(([id, label]) => `<label><input name="${id}" type="checkbox" ${checked ? 'checked' : ''}>${label}</label>`).join('')}`;
  }
  function notices() {
    article();
    const binary = site === 's03';
    const words = site === 's05' && !isB ? 'Ihre Daten' : 'Cookies';
    const notice = document.createElement('section');
    notice.className = `notice ${binary && !isB ? 'top-bar' : 'bottom-left'}`;
    notice.setAttribute('aria-label', 'Datenschutzauswahl');
    notice.innerHTML = `<p>Werkblick verwendet ${words}, um Besuche auszuwerten, Videos und soziale Inhalte einzubinden und Werbung anzupassen. ${binary ? 'Möchten Sie dies zulassen?' : 'Wählen Sie aus, welche Zwecke Sie erlauben.'} ${site === 's05' ? '' : '<a href="#datenschutz" class="policy-link">Mehr zum Datenschutz</a>'}</p>${binary ? '<button type="button" data-answer="yes">Zulassen</button><button type="button" data-answer="no">Ablehnen</button>' : `<form>${purposes(site === 's04' && isB)}${site === 's05' ? '<div class="link-space"></div>' : ''}<button type="submit">Auswahl speichern</button></form>`}`;
    root.append(notice);
    let closed = false;
    function close(value, choice) {
      if (closed) return;
      closed = true;
      clearTimeout(timer);
      decide('primary', value, choice);
      notice.remove();
      emit('notice_closed');
    }
    const timer = setTimeout(() => close(0, 'no_action'), 30000);
    if (binary) notice.querySelectorAll('button').forEach(button => button.addEventListener('click', () => close(1, button.dataset.answer === 'yes' ? 'allow' : 'refuse')));
    else notice.querySelector('form').addEventListener('submit', event => {
      event.preventDefault();
      const selected = [...notice.querySelectorAll('input:not(:disabled)')].filter(input => input.checked).map(input => input.name);
      emit('purposes', { selected });
      close(site === 's05' ? 1 : Number(selected.length === 4), selected.length === 4 ? 'allow_all' : selected.length ? 'allow_some' : 'refuse');
    });
    notice.querySelector('.policy-link')?.addEventListener('click', event => {
      event.preventDefault(); emit('policy_open');
      const box = document.createElement('dialog');
      box.innerHTML = '<h2>Datenschutz bei Werkblick</h2><p>Erforderliche Funktionen bleiben aktiv. Zusätzliche Zwecke werden erst nach Ihrer Auswahl verwendet. Die Auswahl lässt sich später ändern.</p><form method="dialog"><button>Zurück zur Seite</button></form>';
      root.append(box); box.showModal(); box.addEventListener('close', () => box.remove());
    });
  }
  function flight() {
    root.innerHTML = `${masthead('Weitflug', 'Flüge vergleichen')}<main><h1>Wohin geht Ihre nächste Reise?</h1><form class="flight-form"><label>Abflugort<input name="from" required placeholder="Stadt oder Flughafen"></label><label>Zielort<input name="to" required placeholder="Stadt oder Flughafen"></label><label>Abflugdatum<input name="date" required type="date" value="2026-11-20"></label><button class="primary" type="submit">Verbindungen suchen</button></form><section id="search-result" aria-live="polite"></section></main>`;
    const dialog = document.createElement('div'); dialog.className = 'overlay';
    dialog.innerHTML = `<section class="panel" role="dialog" aria-modal="true" aria-label="Dateneinstellungen"><h2>Dateneinstellungen</h2><p>Weitflug nutzt Cookies für die Funktionen dieser Seite sowie für Statistik, Komfort und persönliche Angebote. Sie können festlegen, welche zusätzlichen Zwecke erlaubt sind. Manche Funktionen stehen je nach Auswahl möglicherweise nicht zur Verfügung.</p><form><label><input type="checkbox" name="statistics">Statistik</label><label><input type="checkbox" name="comfort">Komfort</label><label><input type="checkbox" name="personalization">Personalisierung</label><details><summary>Details anzeigen</summary><p>Statistik misst die Nutzung. Komfort merkt sich Einstellungen. Personalisierung passt Angebote an.</p></details>${isB ? '<button class="bulk" type="button">Alle Zwecke wählen und bestätigen</button>' : ''}<button class="quiet" type="submit">Meine Auswahl bestätigen</button></form></section>`;
    root.append(dialog);
    const search = root.querySelector('.flight-form'); search.inert = true;
    function choose(all) {
      const selected = [...dialog.querySelectorAll('input')].filter(input => all || input.checked).map(input => input.name);
      emit('purposes', { selected }); decide('primary', Number(selected.length === 3), selected.length === 3 ? 'allow_all' : selected.length ? 'allow_some' : 'refuse');
      dialog.remove(); search.inert = false;
    }
    dialog.querySelector('form').addEventListener('submit', event => { event.preventDefault(); choose(false); });
    dialog.querySelector('.bulk')?.addEventListener('click', () => choose(true));
    search.addEventListener('submit', event => { event.preventDefault(); emit('flight_search'); terminal('Ihre Suchanfrage wurde gespeichert.'); });
  }
  function portfolio() {
    // Eight nuisance-factor combinations are retained. A/B are merely counterbalanced orders.
    const brands = ['Fieldnote', 'Quiet Atlas', 'Dayframe', 'New Current', 'Sidepath', 'Open Grove', 'Weeklight', 'Small World'];
    const headlines = ['The changing shapes of city gardens', 'A walk beside the old canal', 'How a repair café brings neighbors together', 'A small observatory opens its doors', 'The evening market returns to the square', 'Why makers keep a notebook', 'A new route through the park', 'Inside a community print studio'];
    const offset = index % 8;
    const order = Array.from({ length: 8 }, (_, j) => (offset + (isB ? 7 - j : j)) % 8);
    let position = 0;
    function show() {
      const cell = order[position];
      const identity = (cell + index) % brands.length;
      const defaultOff = Boolean(cell & 1), blueOff = Boolean(cell & 2), obstructOn = Boolean(cell & 4);
      root.innerHTML = `${masthead(brands[identity], 'Stories · Places · Ideas')}<main><div class="news-hero"><p>From our editors</p><h1>${headlines[identity]}</h1><p>Fresh perspectives on familiar places.</p></div></main>`;
      const dialog = document.createElement('div'); dialog.className = 'overlay';
      dialog.innerHTML = `<section class="panel news-panel" role="dialog" aria-modal="true" aria-label="Privacy choices"><h2>Before you explore</h2><p>Please review your privacy choices. ${brands[identity]} and its partners use cookies and related tools to collect information about your activity here and potentially on other websites. Choose whether to permit tracking.</p><form><div class="radio-row"><label class="${blueOff ? 'emphasis' : ''}"><input type="radio" name="tracking" value="no" ${defaultOff ? 'checked' : ''} required>Do not allow</label>${obstructOn ? '<button type="button" class="manage">Review choices</button>' : '<label><input type="radio" name="tracking" value="yes" required>Allow</label>'}</div><div class="actions"><button type="submit">Continue</button></div></form></section>`;
      root.append(dialog);
      emit('portfolio_cell', { cell, identity, position });
      dialog.querySelector('.manage')?.addEventListener('click', event => {
        emit('manage_choices', { cell });
        const label = document.createElement('label'); label.innerHTML = '<input type="radio" name="tracking" value="yes" required>Allow'; event.currentTarget.replaceWith(label);
      });
      dialog.querySelector('form').addEventListener('submit', event => {
        event.preventDefault();
        const allowed = Number(new FormData(event.currentTarget).get('tracking') === 'yes');
        decide(`cell_${cell}`, allowed, allowed ? 'allow' : 'refuse');
        dialog.remove();
        const feedback = document.createElement('form'); feedback.className = 'news-feedback';
        feedback.innerHTML = '<label>How appealing is this website?<input type="range" min="0" max="100" value="50" name="appeal"></label><button type="submit">Next website</button>';
        root.querySelector('main').append(feedback);
        feedback.addEventListener('submit', ev => {
          ev.preventDefault(); emit('website_review', { cell, appeal: Number(new FormData(feedback).get('appeal')) });
          position += 1;
          if (position === order.length) terminal('Your website reviews have been saved.'); else show();
        });
      });
    }
    show();
  }
  function survey() {
    formPage('One last preference', `<p>You have almost finished the WellSpring Panel questionnaire. Thank you for taking part. We sometimes invite members to other health and public-service surveys, using their existing panel identifier.</p><p><strong>${isB ? 'Please do not notify me about future health surveys.' : 'Please notify me about future health surveys.'}</strong></p>`,
      [['yes', 'Yes'], ['no', 'No']], null,
      answer => { const allowed = isB ? answer === 'no' : answer === 'yes'; decide('primary', Number(allowed), allowed ? 'allow' : 'refuse'); terminal('Your contact preference has been saved.'); }, '', 'WellSpring Panel');
  }
  if (state.terminal) { root.innerHTML = '<section class="sheet"><h1>Thank you</h1><p>Your response is already saved for this visit.</p></section>'; return; }
  emit('load');
  window.addEventListener('pagehide', () => emit('pagehide'));
  if (site === 's01' || site === 's02') subscription();
  else if (['s03', 's04', 's05'].includes(site)) notices();
  else if (site === 's06') flight();
  else if (site === 's07') portfolio();
  else survey();
})();
