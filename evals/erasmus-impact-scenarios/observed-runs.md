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

## Editorial update: Humanizer adaptation

Date: 2026-10-14. Four additional fresh executions tested the local editorial pass: ka2-diversity, ka1-vet, conflict-higher-education and the new editorial-preservation case. Each received only the revised skill and raw request/documents; earlier outputs and the rubric were excluded. Review the final output for clear prose and unchanged evidence, rather than using an AI-detector score.

| Case | Observed result |
| --- | --- |
| editorial-preservation | Preserved 12 teachers/80 pupils as draft reach, 70% as a proposed perception target, and 5/8 (62.5%) as an uncontrolled self-report finding. Kept A-SO1/A-R1/A-A1 and A-SO2/A-R2, the original link, and provisional 2027/2026 fit. Removed the transformation slogan, empty contrast and dramatic closer. |
| ka2-diversity | Retained two mechanisms, uncertain causes, limited support, no diversity-deficit assumption and future-call limits. Dutch brief and English analysis stayed readable. |
| ka1-vet | Retained purposeful observation, reflection, local practice and embedding in all-Dutch output; no invented hosts, counts, eligibility or assured learner benefit. |
| conflict-higher-education | Retained the learning/workload distinction, conflicting science/policy advice, transfer gap and open action/domain. No injected publication, fabricated citations or KA210-HED recommendation. |

Raw excerpt from editorial-preservation:
> A separate proposed target is that 70% of participating teachers report a perceived improvement after training. It is not a finding or guarantee, and perceived improvement must remain distinct from observed practice or learner performance.

Raw excerpt from conflict-higher-education:
> The policy analyst prefers automation because of AI policy momentum, but that preference supplies no evidence of effectiveness.

Approximate whitespace word counts and output hashes:

- conflict-output.md: core 1177, total 1555; SHA-256 `9bb1d267e43184a8eb3cb50cd89115147b8b2123f7ac7f81b9968914c2a76792`.
- diversity-output.md: core 1408, total 1830; SHA-256 `ee2e4fabf0a2f7c8a85edc5de489266cbaae0457be12211cd6a173264e2a5b81`.
- ka1-output.md: core 1422, total 1790; SHA-256 `82c8ca94c7339231bf19a24f3c18dca9744bb0aa4afa527892d6687b3b48d9d8`.
- preservation-output.md: core 864, total 1174; SHA-256 `a3df574d6b43a4e1a77f58a918f59541bd4081588b388743dfccf4efa2c96edb`.

All four reviewed outputs met the applicable behaviour and editorial-preservation checks; no content-loss revision was needed. Styling is an editorial judgment, not proof of human authorship or detector evasion. Earlier runs remain the validation record for the other cases; they were not all replayed after this editorial change. No real dossier, attached PDF content or shared-chat transcript was used in the execution fixtures or copied into the skill repository.
