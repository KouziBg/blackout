"""Vérifie que la logique du jeu ne dépend pas de pygame."""

import ast
from pathlib import Path

import pytest

SRC = Path(__file__).parents[1] / "src" / "blackout"
LOGIC_FILES = [
    path
    for folder in ("world", "entities", "ai")
    for path in sorted((SRC / folder).glob("*.py"))
]


def imported_modules(path: Path) -> set[str]:
    modules: set[str] = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


@pytest.mark.parametrize("path", LOGIC_FILES, ids=lambda p: p.name)
def test_logic_never_imports_pygame(path: Path) -> None:
    assert not any(name.split(".")[0] == "pygame" for name in imported_modules(path))
