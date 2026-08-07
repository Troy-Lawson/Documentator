from pathlib import Path

import pytest

from loaders.structure import load_structure


def test_load_structure_includes_page_content(tmp_path: Path) -> None:
    structure = tmp_path / "structure.yaml"
    structure.write_text(
        """
title: Handbook
body: Root body
labels: [docs]
children:
  - title: Onboarding
""".strip(),
        encoding="utf-8",
    )

    root = load_structure(structure)

    assert root.title == "Handbook"
    assert root.body == "Root body"
    assert root.labels == ["docs"]
    assert [child.title for child in root.children] == ["Onboarding"]


def test_load_structure_rejects_non_mapping_yaml(tmp_path: Path) -> None:
    structure = tmp_path / "structure.yaml"
    structure.write_text("- not\n- a\n- page", encoding="utf-8")

    with pytest.raises(TypeError, match="YAML mapping"):
        load_structure(structure)
