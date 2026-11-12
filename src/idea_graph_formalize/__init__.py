"""Пакет «Формализация требований»: скилл и манифест."""

from pathlib import Path

__version__ = "0.1.0"


def manifest() -> dict:
    return {
        "id": "formalize",
        "name": "Формализация требований",
        "description": "Превращает принятые решения в функциональные требования с критериями приёмки. "
                       "Спрашивает только там, где решение можно понять по-разному.",
        "kind": "agent",
        "order": 30,
        "reads": ["идея", "ветка", "решение", "граница"],
        "writes": ["требование"],
        "asks": True,
        "web_search": False,
        "model_level": "средняя",
        "outcomes": ["готово"],
        "fresh_session": True,
        "skill": (Path(__file__).parent / "skill.md").read_text(encoding="utf-8"),
    }
