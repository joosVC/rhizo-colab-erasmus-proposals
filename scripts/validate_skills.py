#!/usr/bin/env python3
"""Check the repository's deliberately minimal skill format and local references.

This checks structure, not workflow behaviour or external integration. No dependencies.
"""

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def check_skill(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: (\"[^\n]+\")\n---\n", text)
    require(match is not None, f"{path.relative_to(ROOT)}: expected name + quoted description frontmatter")
    if match:
        name, raw_description = match.groups()
        require(name == path.parent.name and len(name) <= 64, f"{path}: skill name/folder mismatch")
        require(not name.startswith("-") and not name.endswith("-") and "--" not in name, f"{path}: invalid name")
        try:
            description = json.loads(raw_description)
            require(0 < len(description) <= 1024, f"{path}: description length")
        except json.JSONDecodeError:
            ERRORS.append(f"{path}: description must be a valid quoted string")
    require(len(text.splitlines()) < 500, f"{path}: keep core instructions under 500 lines")
    require("TODO" not in text and "TBD" not in text, f"{path}: unresolved authoring placeholder")
    metadata = path.parent / "agents" / "openai.yaml"
    require(metadata.is_file(), f"{path}: missing agents/openai.yaml")
    if metadata.is_file():
        config = metadata.read_text(encoding="utf-8")
        for key in ("display_name", "short_description", "default_prompt"):
            require(re.search(rf"^  {key}: .+", config, re.MULTILINE) is not None, f"{metadata}: missing {key}")
        require(f"${path.parent.name}" in config, f"{metadata}: default prompt must name the skill")
        short = re.search(r'^  short_description: "(.*)"$', config, re.MULTILINE)
        require(short is not None and 25 <= len(short.group(1)) <= 64, f"{metadata}: short description length")
    for folder in ("references", "assets"):
        for resource in (path.parent / folder).glob("*.md"):
            target = f"{folder}/{resource.name}"
            require(f"]({target})" in text, f"{resource}: not directly linked from SKILL.md")


def check_links(path):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        require((path.parent / target).exists(), f"{path.relative_to(ROOT)}: broken local link {target}")


def check_policy_register(path):
    """Validate discovery metadata, without claiming live source verification."""
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
        require(record["schema_version"] == 1, f"{path}: unsupported register schema")
        require(record["call_year"] == int(path.parent.name), f"{path}: call year/folder mismatch")
        date.fromisoformat(record["checked_on"])
        documents = record["documents"]
        require(isinstance(documents, list) and bool(documents), f"{path}: missing documents")
        ids = [item["id"] for item in documents]
        require(len(ids) == len(set(ids)), f"{path}: duplicate source IDs")
        roles = {"programme-guide", "annual-work-programme", "awp-amendment", "guide-corrigendum", "call-notice"}
        for item in documents:
            for field in ("id", "issuer", "title", "identifier", "notes"):
                require(isinstance(item[field], str) and bool(item[field]), f"{path}: missing {field}")
            require(item["role"] in roles, f"{path}: unsupported document role")
            date.fromisoformat(item["document_date"])
            require(item["verified_level"] in {"metadata-only", "metadata-and-selected-sections", "full-document"}, f"{path}: invalid verification level")
            require(isinstance(item["locators"], list) and all(isinstance(x, str) for x in item["locators"]), f"{path}: invalid locators")
            for field in ("landing_url", "download_url"):
                url = item[field]
                if field == "download_url" and url is None:
                    continue
                parsed = urlparse(url)
                require(parsed.scheme == "https" and bool(parsed.hostname), f"{path}: invalid {field}")
            digest = item["sha256"]
            require(digest is None or (isinstance(digest, str) and re.fullmatch(r"[a-f0-9]{64}", digest) is not None), f"{path}: invalid checksum")
        require({"programme-guide", "annual-work-programme"}.issubset({item["role"] for item in documents}), f"{path}: missing baseline document role")
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        ERRORS.append(f"Invalid policy register {path}: {exc}")


def main():
    skills = sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    require(bool(skills), "No skills found")
    for path in skills:
        check_skill(path)
    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            check_links(path)
    for skill in skills:
        cases_path = ROOT / "evals" / skill.parent.name / "cases.json"
        try:
            cases = json.loads(cases_path.read_text(encoding="utf-8"))["cases"]
            ids = [case["id"] for case in cases]
            require(bool(cases), f"{cases_path}: empty evaluation cases")
            require(len(ids) == len(set(ids)), f"{cases_path}: duplicate evaluation case IDs")
            for case in cases:
                require(isinstance(case["opening"], str) and bool(case["opening"]), f"{case['id']}: missing opening")
                require(isinstance(case["turns"], list) and all(isinstance(t, str) for t in case["turns"]), f"{case['id']}: invalid turns")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            ERRORS.append(f"Invalid evaluation cases in {cases_path}: {exc}")
    for register in (ROOT / "policy-sources").glob("*/manifest.json"):
        check_policy_register(register)
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(skills)} skill(s); metadata, resource links, evaluation inputs and available policy registers checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
