# Repository guidance

Maintain this repository as the shared source for RHIZO Erasmus+ proposal-development skills.

- Keep authoring instructions in English; keep teacher-facing conversations and start notes in Dutch. Elicit briefs and future concept-writing outputs use English unless explicitly requested otherwise.
- Honour explicit user requirements over skill defaults. Distinguish editing a skill from invoking its participant workflow.
- Keep each skill focused on one phase. The first skill captures accounts and unknowns; it does not research, score funding prospects, select partners/calls, or require a Theory of Change.
- Use precise YAML name/description metadata, concise SKILL.md instructions and directly linked supporting references/assets. Avoid duplicating full workflows across files.
- Keep the Elicit brief phase prompt-only: preserve intake uncertainty, explore established/emerging evidence and relevant adjacent fields, and hand off to user-run Elicit research. Do not prewrite findings, require a ToC or start API runs. Scientific exploration and policy screening feed provisional impact scenarios before the team choice meeting; PRP follows the refined impact design.
- Use the Dutch National Agency Impact Tools for provisional KA1/KA2 scenario design. Keep objectives as changes, outputs/activities as their supports and causal assumptions visible. Use KA2 knowledge development/application/embedding flexibly; keep KA1 mobility learning and transfer coherent. Do not force three scenarios, fabricate evidence/commitments or equate product availability with sustainability.
- Keep policy screening source-grounded: verify call-year documents/amendments, read original policy passages, distinguish formal fit from momentum, and disclose actual coverage. A source register is a locator, not a current verified corpus. Future-year fit remains provisional until its call is read. Give diagnostic judgments, not grant points/probabilities.
- Use synthetic cases for evaluations. Keep private proposals, real intake transcripts, identifiable student data and credentials out of the skill source repository, even though it is private.
- Run `python3 scripts/validate_skills.py` after changes. For behavioural changes, replay relevant cases from that skill's `evals/<skill>/cases.json` and review with its rubric. Give execution agents only the skill and raw task inputs, not evaluator expectations.
- Describe the actual scope of validation. A text simulation does not establish voice-client integration, installation, funding quality or classroom effectiveness.
- Keep GitHub publication distinct from installation in a colleague's ChatGPT account. Do not claim a plugin was installed or published without evidence.
