from pathlib import Path

import yaml

from models.page import Page


def load_structure(path: Path) -> Page:
    """Load a documentation structure from a YAML file."""
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise TypeError("Structure file must contain a YAML mapping")

    return _parse_node(data)


def _parse_node(node: dict) -> Page:
    """Recursively build a Page tree."""
    page = Page(
        title=node["title"],
        body=node.get("body", ""),
        labels=node.get("labels", []),
    )

    for child in node.get("children", []):
        page.add_child(_parse_node(child))

    return page
