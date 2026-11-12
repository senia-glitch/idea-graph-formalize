from importlib import metadata

from ideagraph_formalize import manifest


def test_manifest_is_complete():
    m = manifest()
    assert m["id"] == "formalize" and m["kind"] == "agent" and m["outcomes"] == ["готово"]
    assert m["web_search"] is False
    for phrase in ['formalize.acceptance', 'FR-1', 'proposed', 'finish']:
        assert phrase in m["skill"]


def test_entry_point_is_declared():
    assert "formalize" in [p.name for p in metadata.entry_points(group="ideagraph.packages")]
