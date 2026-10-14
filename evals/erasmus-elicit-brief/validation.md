# Validation scope

The skill prepares an English research brief from a supplied starting account. It does not execute Elicit or validate a scientific report. All behavioural inputs are synthetic; no live account, API, school intake or student data is used.

## Checks

See [cases](cases.json), [rubric](rubric.md) and [actual excerpts](observed-runs.md). Fresh execution agents received the skill and raw request only; evaluator expectations were withheld.

The repository validator passed with both skills: metadata, directly linked resources, Markdown links and evaluation input structure. The bundled skill-creator validator passed for the new skill. The modified stdlib validator was executed and compiled successfully. These checks do not establish behavioural correctness.

## Behavioural results: seven cases, eight fresh executions

| Case | Observation |
| --- | --- |
| Group-work participation | Immediate draft, uncertainty retained, explicit measurement question preserved |
| Surfing | Initial current/planned-practice error corrected through an explicit provenance instruction; fresh replay preserved both existing practice and proposed intervention |
| AI literacy | Entirely English, Agent workflow respected, judgement-versus-knowledge assessment retained |
| Environmental citizenship | PAR method/intervention distinction; collective action outcomes and adjacent lenses retained |
| Sparse inclusion | No extra questions, unknowns retained, invented proof and Erasmus novelty declined |
| Missing input | Single request for the absent note/location |
| Returned report fragment | Completion acknowledged as user-reported; no invented findings or automatic ToC; next task clarified |

Every completed prompt requested established/emerging evidence, source-backed uncertainty, contrary findings, contextual fit and an evidence-linked shortlist rather than prewriting conclusions. Execution status remained prompt-only. All seven cases satisfied the reviewed rubric after the surfing correction; the initial run's fidelity issue remains visible in the excerpts. Only the affected case was replayed after the one-line provenance revision; this is not a claim that every case was rerun on the final version.

## Limits

Elicit has not run the generated prompts in this validation. Scientific coverage, adherence to requested comparison fields, actual report quality, voice use and colleague installation remain untested. The next external check is a user-run Elicit pilot retaining the prompt, report, references and available search/extraction data.
