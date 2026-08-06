from pathlib import Path

import yaml

from models.page import Page


def load_structure(path: Path) -> Page:
    """Load a documentation stucture from a YAML file"""

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return _parse_node(data)


def _parse_node(node: dict) -> Page:
    """Recursively build a Page tree."""

    page = Page(
        title=node["title"]
    )

    for child in node.get("children", []):
        page.children.append(_parse_node(child))

    return page