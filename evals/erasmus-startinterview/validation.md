# Validation — initial version

Date: 13 October 2026. Status: ready for a teacher pilot; synthetic text behaviour evaluated, real voice integration not evaluated.

## Structural checks

- Initialised with the skill-creator initializer.
- Passed the bundled skill-creator `quick_validate.py` frontmatter/name check.
- Generated Dutch display metadata and invocation prompt with the skill-creator metadata generator.
- Passed `python3 scripts/validate_skills.py`: minimal frontmatter, folder naming, UI metadata, direct resource links, local Markdown links and evaluation-input shape.
- Compiled and executed the repository validation script. GitHub Actions repeats the structural check; it does not run behavioural simulations.

## Behavioural checks

Used six independent interviewer contexts with the skill and its referenced resources, without expected answers or the evaluation rubric. Delivered the scripted participant messages one turn at a time. Reviewed the actual replies and reports against [the rubric](rubric.md). Raw input scenarios are in [cases.json](cases.json); literal output excerpts are in [observed-runs.md](observed-runs.md).

| Scenario | Observed outcome | Result |
| --- | --- | --- |
| Broad diversity need | Asked for a real classroom episode, kept language/trust as uncertain explanations, checked remaining availability, and recommended Joos without requiring a solution or numbers | Pass |
| Personal theater interest | Retained the interest and existing annual practice, avoided asserting learning effects, and recommended internal alignment because extra lesson time would involve colleagues | Pass |
| Group transferring a project | Preserved differing views, unverified project name and doubled-participation claim; handled extended availability; recommended clarification without treating leadership interest as project approval | Pass |
| Sparse immediate stop | Delivered a short note immediately, marked unknown/unspoken topics, and avoided deriving school-wide support from ‘we’ | Pass |
| Explicit English override | Conducted the opening and short output in English; preserved unknowns rather than padding | Pass |
| Explicit research/concept handoff | First response was overly meta; after instruction revision, a fresh replay addressed the user directly and requested only the unavailable prior note | Pass after revision |

No intake run performed web research or required a complete Theory of Change. All report requests were honoured without a compulsory extra question. Conversation and report quality were reviewed manually; this is not a statistical benchmark or a guarantee across models.

## Revision from testing

Clarified the phase-change instruction: respond directly to the user, reuse an available note, request only missing input, and do not explain the skill's internal permission logic. Replayed that scenario in a new context and reran structural validation. The other five runs preceded this narrow boundary revision; their interview instructions were unchanged.

## Remaining validation

- Try with RHIZO teachers using the actual intended speech/dictation interface; measure whether the conversation fits their available time.
- Check spoken pacing, transcription ambiguity, long answers, mixed speakers and the report's usefulness to Joos and leadership.
- Confirm the selected environment loads all supporting files and whether installation/plugin distribution is required there.
- Evaluate subsequent research and English concept-writing workflows separately; they are not implemented here.

No real teacher interviews, pupil records, private proposals or school survey data were published. GitHub publication is the shared source delivery, not installation in colleagues' accounts.
