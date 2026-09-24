# Ledger anchors

Mimiq's [sealed prediction ledger](https://www.mimiqai.com/ledger) records Mimiq's call on
a live A/B test before its result exists. Each entry publishes only a salted sha256 of the
call and a chain hash that links it to every entry before it. The call and the salt are
revealed when the owner reports the real result, and anyone can recompute both hashes.

Once a day, a GitHub Action in this repository fetches the public ledger and appends a line
to `anchors.jsonl`: the time, the number of entries, the last entry's number, the chain head,
and the sha256 of the whole public list. `latest.json` is that day's copy of the list.

Because GitHub records when each anchor commit was pushed, anyone can check that an entry
existed by a given day, and that no entry was later added, removed or reordered: every
later head has to extend the earlier ones.
