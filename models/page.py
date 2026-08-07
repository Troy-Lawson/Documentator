from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Page:
    title: str
    body: str = ""
    labels: list[str] = field(default_factory=list)
    children: list[Page] = field(default_factory=list)

    def add_child(self, page: Page) -> None:
        self.children.append(page)

    def __str__(self) -> str:
        return self._format_tree()

    def _format_tree(self, level: int = 0) -> str:
        indent = " " * level
        lines = [f"{indent}- {self.title}"]

        for child in self.children:
            lines.append(child._format_tree(level + 1))

        return "\n".join(lines)
