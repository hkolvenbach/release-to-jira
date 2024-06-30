import os
import re

PROJECT = os.environ["INPUT_JIRA_PROJECT"]
ISSUE_PATTERN = rf"{PROJECT}-[0-9]+"
CHANGES_SECTION = "What's Changed"

def _parse_changelist(content):
    items = []
    for line in content.split("\n"):
        try:
            issue_id = extract_issue_id(line)
            items.append(
                {
                    "issue_id": issue_id,
                    "content": line
                }
            )
        except Exception as ex:
            print('skipped', line, ex)
    return items


def extract_changes():
    with open("notes.md", "r") as f:
        content = f.read()

    return _parse_changelist(content)


def extract_issue_id(change):
    matches = re.findall(ISSUE_PATTERN, change)
    if not matches:
        return None
    return matches[0]
