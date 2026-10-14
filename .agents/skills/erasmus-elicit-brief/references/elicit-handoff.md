# Handoff to Elicit

## Default: user-run Research Report

Prepare one English prompt with a clear question first, followed by context, scope and requested synthesis. Tell the user to paste it into Elicit's Research Report workflow, review any suggested changes against the intended scope, and generate the report using their available account options. Requested comparison structure is a specification, not a guarantee of Elicit compliance or completeness.

If the user already works in the Research Agent, the same structured brief can request a cited report there. Do not require a switch. If detailed instructions do not fit or the user wants greater control over output, the Agent is an alternative; do not invent a character limit or assume access to a specific plan feature. A Systematic Review is a separate choice for explicit screening/extraction control, not the default for this exploratory phase.

Offer a compact question plus the longer brief only when useful, clearly labelling where the additional instructions must also be supplied. Do not present a compact question as equivalent to the full brief. Avoid unverified button-by-button directions; consult current official help only if exact interface guidance is requested.

## End of this step

The skill delivers the prompt; the user executes it. Say: “De prompt is klaar; het onderzoek is nog niet uitgevoerd. Voer hem uit in Elicit en bewaar het rapport met deze prompt en de uitvoerdatum.” Adapt to the user's language and any actual execution evidence.

Retain the original research question/brief, run date, report and reference list; keep search/screening/extraction exports too if available and useful. They support later checking and discussion. The returned report ends the scientific exploration stage, but does not by itself establish that its claims are verified or select a project direction.

Next: complete EU policy screening, then combine the practice account and both reports into provisional impact scenarios for discussion with Joos/project owner. The team chooses and refines a direction; PRP screening follows the refined impact design. The erasmus-impact-scenarios skill supports that synthesis as a separate task; PRP and concept-writing skills are not yet implemented. If a completed report arrives, do not restart the intake or automatically synthesize a ToC. Follow an explicit request to interpret it as a new task.

## Integration boundary

No API or MCP execution is implemented in this skill. Do not request or store API keys, initiate paid runs, upload the intake or imply account/team sharing was configured. Reduce the prompt to research-relevant, non-identifying context for manual use as well.

For a separately requested integration, recheck Elicit's current API docs, terms, subscription and credential arrangement. Keep secrets out of source control and client code. The API terms checked on 2026-10-14 prohibit submission of personal data and restrict standalone access/key sharing, with a conditional employee exception for organisational internal use. Do not assume a personal Pro key may be distributed to RHIZO colleagues. This is context for future integration, not an approval step for preparing a prompt.
