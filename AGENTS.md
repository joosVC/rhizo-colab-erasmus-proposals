# Repository guidance

Maintain this repository as the shared source for RHIZO Erasmus+ proposal-development skills.

- Keep authoring instructions in English; keep teacher-facing start interviews, question examples and start notes in Dutch. Future concept-writing workflows use English outputs.
- Honour explicit user requirements over skill defaults. Distinguish editing a skill from invoking its participant workflow.
- Keep each skill focused on one phase. The first skill captures accounts and unknowns; it does not research, score funding prospects, select partners/calls, or require a Theory of Change.
- Use precise YAML name/description metadata, concise SKILL.md instructions and directly linked supporting references/assets. Avoid duplicating full workflows across files.
- Use synthetic cases for evaluations. Do not commit private proposals, real intake transcripts or identifiable student data to this public repository.
- Run `python3 scripts/validate_skills.py` after changes. For behavioural changes, replay relevant cases from `evals/erasmus-startinterview/cases.json` and review with the rubric. Do not load evaluator expectations into the interviewer agent.
- Describe the actual scope of validation. A text simulation does not establish voice-client integration, installation, funding quality or classroom effectiveness.
- Keep GitHub publication distinct from installation in a colleague's ChatGPT account. Do not claim a plugin was installed or published without evidence.
