# Impact-scenario skill validation

Date: 2026-10-14.

## Method

Initialize the skill with the skill-creator script, generate its interface metadata, validate its frontmatter and run the repository structure/link checks.

Forward-run all six synthetic cases in independent fresh execution threads. Give each thread only the skill location and raw opening/documents, not the rubric, expected answers, prior reports or evaluation diagnoses. Read the resulting outputs against the rubric. Claims inside fixtures are invented test data; this exercise does not validate their scientific truth.

## Initial observations and revision

All six outputs preserved the requested route/language, provenance and uncertainty boundaries. The KA2 cases supported meaningful alternatives where warranted and one limited hypothesis where alternatives were not justified. The missing-science case recognised an unexecuted Elicit prompt; the conflict case rejected embedded instructions and retained scientific-policy disagreement. The no-input case requested context instead of inventing a dossier.

Two outputs were too long for a practical team pre-read: the diversity and KA1 cases. Revise the skill and template with a core word ceiling, shorter scenario cards, compact tables and a grouped source appendix. Re-run those two cases in fresh threads on the same raw inputs.

## Final outcome

Six synthetic cases were executed and reviewed. The two length cases were repeated in independent fresh threads after revision: diversity produced a 1,451-word core and KA1 a 1,476-word core, both below the 1,700-word ceiling. Their sources annexes remained separate and the important evidence/route caveats remained in the core. Word counts are approximate whitespace counts, including Markdown table tokens.

All six cases met the behavioural criteria after the two length replays. The four other cases needed no behavioural revision; their input-handling boundaries and outputs were reviewed against the updated format. Final checks passed: creator frontmatter validation, four-skill repository metadata/resource/link/evaluation/register checks and git diff whitespace validation. See [observed runs](observed-runs.md) for raw excerpts, output hashes and the first-pass length finding.

The final repository-wide check covers structure; it does not execute all earlier skills. No simulated result is presented as real research or a confirmed funding prospect.

## Limits

This is text-based synthetic forward-testing, not testing in a teacher meeting. No real Elicit report, live policy scan, original study accuracy, voice client, account installation, formal application scoring or educational impact was validated. The national tools' pages, blank worksheet and selected handbook/action sections inform the method; the linked interactive examples were not readable through text retrieval.

Existing Elicit and policy skills receive only handoff-sequence wording changes. Their research/prompt workflows are not redesigned or re-evaluated here; structure checks cover the full repository. Published GitHub content remains separate from colleagues' account installation.

## Editorial update

Add a local, attributed adaptation of blader/humanizer v3.1.0 at commit 225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8, with its MIT licence. Require prose editing followed by an invariant check on numbers, mappings, sources, causal strength and uncertainty. Preserve the language and scenario-design contract; no external installation is required.

Four additional independent fresh executions passed the reviewed checks: ka2-diversity, ka1-vet, conflict-higher-education and editorial-preservation. The last adds exact figures, targets, identifiers and a source link to test content preservation. The registry now contains seven cases; this update replays four relevant cases, not all seven. See observed-runs.md for raw excerpts, approximate lengths and hashes.

The editorial pass improves professional readability; these tests do not validate AI detection, scientific effectiveness or funding quality. Interface metadata stays unchanged because the skill's identity, trigger and primary output remain the same. Creator validation, repository validation and diff whitespace checks pass.
