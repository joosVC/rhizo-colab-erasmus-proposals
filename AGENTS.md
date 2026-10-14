# Repository guidance

Maintain this repository as the shared source for RHIZO Erasmus+ proposal-development skills.

- Keep authoring instructions in English; keep teacher-facing conversations and start notes in Dutch. Elicit briefs and future concept-writing outputs use English unless explicitly requested otherwise.
- Honour explicit user requirements over skill defaults. Distinguish editing a skill from invoking its participant workflow.
- Keep each skill focused on one phase. The first skill captures accounts and unknowns; it does not research, score funding prospects, select partners/calls, or require a Theory of Change.
- Use precise YAML name/description metadata, concise SKILL.md instructions and directly linked supporting references/assets. Avoid duplicating full workflows across files.
- Keep the Elicit brief phase prompt-only: preserve intake uncertainty, explore established/emerging evidence and relevant adjacent fields, and hand off to user-run Elicit research. Do not prewrite findings, require a ToC or start API runs. Policy screening and a choice discussion precede the provisional ToC; PRP follows it.
- Use synthetic cases for evaluations. Keep private proposals, real intake transcripts, identifiable student data and credentials out of the skill source repository, even though it is private.
- Run `python3 scripts/validate_skills.py` after changes. For behavioural changes, replay relevant cases from that skill's `evals/<skill>/cases.json` and review with its rubric. Give execution agents only the skill and raw task inputs, not evaluator expectations.
- Describe the actual scope of validation. A text simulation does not establish voice-client integration, installation, funding quality or classroom effectiveness.
- Keep GitHub publication distinct from installation in a colleague's ChatGPT account. Do not claim a plugin was installed or published without evidence.
