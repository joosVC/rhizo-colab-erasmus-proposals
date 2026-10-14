# Baseline and call-year updates

## Use the register correctly

The repository stores discovery metadata by call year in `policy-sources/<year>/manifest.json`. It does not embed the full Guide, certify that all amendments were read, or hold confidential dossier reports. Load the matching register through an available filesystem or connector; use official pages if a register is absent. Source IDs and locator notes are internal aids.

Register `verified_level` describes maintainer inspection on `checked_on`. It is not live verification. A `metadata-only` amendment entry establishes its existence/identifier only, not its effects. A null download URL means obtain the attachment from the official page; do not manufacture a URL. A null checksum means no source bytes were archived/hashes verified. During a run, record actual retrieved versions, read coverage and conflicts in the report ledger.

## New documents supplied by the user

Validate document identity first. Check whether the new material is an Erasmus+ call document, draft or unrelated Commission work programme. A file named “2027” is not enough. Compare the relevant official/current text; if browsing is unavailable, say the supplied document's currency could not be checked.

For an explicitly requested repository baseline update:

1. Add a new year register; preserve the previous year's record.
2. Record issuer, official title/identifier, version/date, landing/download URLs, check date and actual verification level. Use real hashes only for archived bytes.
3. Inspect Guide priorities, relevant action scope/award text, AWP policy sections and operative amendments.
4. Write a concise relevant change note: added/removed/reworded priorities, action scope changes, changed policy emphasis and unresolved items. Distinguish substantive changes from formatting/reordering.
5. Check metadata/links and replay future-year, sector-route and conflicting-version cases before publishing the update.

Keep ordinary dossier scans separate from source-repo updates. An intake does not authorise publishing its report. Do not silently edit a shared baseline merely because browsing discovers newer material.

## Unpublished or inaccessible call year

Search official pages once plus a targeted official search before deciding the requested year was not located. Phrase this as what was found on the research date, not proof of universal non-existence. Use the newest read earlier-year baseline, identify it explicitly and retain current policy research. Put the future-year caveat beside fit judgments. Never transfer budgets, priorities, deadlines or national emphases to a future call as confirmed facts.

If an amendment is known but unread, state that limitation and identify which judgments it affects. Do not label the whole scan verified/current if only original documents were read. Distinguish Guide-based priority mapping from AWP-specific emphasis or changes still to be checked.
