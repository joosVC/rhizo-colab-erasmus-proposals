# Validation scope

This skill performs policy research rather than generating an Elicit prompt. The evaluation uses synthetic project accounts, an actual 2026 Guide for document-only cases, and clearly labelled synthetic source metadata for status/data checks.

See [cases](cases.json), [rubric](rubric.md) and [actual output excerpts](observed-runs.md). Evaluation sources are not a confidential dossier corpus. No Elicit/API keys, student records, live applications or person-directed messages are involved.

## Structural checks

The repository validator passed with three skills and the 2026 register. The bundled skill-creator validator passed for the new skill. The added register checks were exercised against actual valid metadata and three temporary malformed variants: wrong call year, invalid date and duplicate source ID. All four checks produced the expected result. No temporary fixtures were committed.

## Reviewed behavioural runs: six cases, eight fresh executions

| Case | Observation |
| --- | --- |
| Live school/AI | First run disclosed unread AWP amendment; fresh replay used improved register and read replacement annex, preserving language and policy/evidence distinctions |
| Live VET/outcomes | Actual original policy/research documents read, including the operative amended AWP; English override and country uncertainty retained |
| Offline future year | 2026 source kept distinct from unverified target 2027; no live scan claimed |
| Offline HED/action route | Scope mismatch and invented funding-score request handled correctly; initial language split missed, instruction revised and fresh replay passed |
| Synthetic data/status | Measurement/publication/adoption distinctions, no local extrapolation, no invented sources |
| Missing input | Single request for actual starting account |

The amended AWP was recovered during the live VET run. The parent independently opened the official PDF, inspected its replacement clause and selected relevant passages, and added the actual download URL/coverage to the register. The language revision and source-register improvement were followed by fresh affected-case replays; other original cases were not all rerun on the final version.

The six cases met the reviewed criteria after the HED language correction. Three executions involved real public-source browsing (two school runs and one VET run); five were document-only or missing-input checks, including the HED replay. The school replay still disclosed unavailable full research reports and unverified national emphasis instead of overstating coverage. Diagnostic judgments were reasoned but not calibrated against real grant evaluators.

## Limits

The final source register contains inspected metadata and selected sections, not archived source bytes or an assurance of all relevant provisions for every dossier. A live run must recheck current versions and read pertinent passages. Structural validation cannot establish source currency. These cases do not establish exhaustive policy coverage, live 2027 eligibility, real-colleague usability, installation or grant success. The next user check is a real starting note with its report/source ledger, before any ToC synthesis.
