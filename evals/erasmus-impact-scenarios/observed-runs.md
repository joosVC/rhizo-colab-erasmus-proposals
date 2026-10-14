# Observed impact-scenario runs

Date: 2026-10-14. Six raw cases were executed in independent fresh threads; two were replayed after a length revision. Execution prompts supplied only the skill path and raw request/documents. The outputs were reviewed against the rubric afterwards. All practice/science/policy inputs were explicitly synthetic.

## Results and raw excerpts

### ka2-diversity

Outcome: pass on the reviewed final output. Two mechanisms, no diversity-causality assumption; 2027 remains provisional; no action/budget selection.

Raw excerpt:
> Meer diversiteit is geen aangetoonde verklaring en vormt op zichzelf geen onderwijsprobleem.

Approximate core / total whitespace words: 1451 / 1913.
Output SHA-256: `36fd189cbab9d461b145adac42b19fc04c87356e82633605b9de53fd4ca7b942`.

### ka2-water-transfer

Outcome: pass on the reviewed final output. One bounded transfer route, adjacent evidence limits; existing water practice retained, no compulsory WPs.

Raw excerpt:
> This is a transfer hypothesis: water exposure alone is not the demonstrated mechanism (C2–C3).

Approximate core / total whitespace words: 1127 / 1399.
Output SHA-256: `2a8838242e6cc7b6e49baf09b017fdf1f2431dcb595f26b480ac701ae5c97c94`.

### ka1-vet

Outcome: pass on the reviewed final output. Explicit Dutch output; two learning/transfer routes; no product portfolio, hosts, counts or grant amounts.

Raw excerpt:
> Een reisverslag delen zorgt voor bereik; herhaald oefenen en afgesproken opvolging dragen de verankering.

Approximate core / total whitespace words: 1476 / 1940.
Output SHA-256: `cb0d6fffdcbc999fe42b7aae3e8a7c93ab02d31404bf7b2eefea6736d38f8e38`.

### missing-science

Outcome: pass on the reviewed final output. Prompt not treated as completed research; limited hypothesis and local/research-first alternative.

Raw excerpt:
> S is an unexecuted research prompt, not a completed report.

Approximate core / total whitespace words: 1524 / 1883.
Output SHA-256: `692a9de7152f59bf3c7858ad0a8fbebd889c271896c337bd59712a8c92feeb34`.

### conflict-higher-education

Outcome: pass on the reviewed final output. Explicit English output; disagreement and workload gap retained; no fabricated citations, KA210-HED recommendation or publication.

Raw excerpt:
> policy momentum supports investigation, not intervention effectiveness.

Approximate core / total whitespace words: 1390 / 1762.
Output SHA-256: `1e755362870a200957526ecb555fc498a5a6e16a3ab5bc1c450b9288486c747d`.

### no-input

Outcome: pass on the reviewed final output. One brief request for project context; no invented dossier or scenarios.

Raw excerpt:
> Een concrete ervaring of eerste projectidee is voldoende; een uitgewerkte startnotitie is nog niet nodig.

Approximate core / total whitespace words: 97 / 97.
Output SHA-256: `9744d9a1eaf7af5b35e4a66d09f28237c92d1de5c963ed0257fb9f12e990c3c9`.

## First-pass issue and replay

The first reviewed diversity and KA1 outputs were too long for a practical team pre-read, even though their input handling and design logic were sound. The saved first-review snapshots had total whitespace word counts of 3,100 and 2,843. Revise the core/template to set a 1,700-word core ceiling, short cards, combined supporting paragraphs and a compact grouped source appendix.

Re-run the same raw requests in fresh threads with no earlier outputs or explanation of the expected improvement. Final cores were 1,451 and 1,476 words; total counts were 1,913 and 1,940. The shorter packs retained causal assumptions, conditional advice, input provenance, route limitations and team questions. The other final cores also fit the ceiling.

## Evidence and scope

The full generated reports were inspected during this work; selected raw excerpts and content hashes are retained here. The transient full run files are not part of the shared skill repository. Reproduce the tasks from cases.json, using each opening and input; output wording can vary.

No actual Elicit study findings, live policy analysis, private teacher records, installed client, teacher meeting or educational effects were tested. Do not reuse fixture claims or their apparent policy dates as real evidence. Future field use must assess whether the team finds the cards understandable and whether the chosen assumptions and measurements are useful.
