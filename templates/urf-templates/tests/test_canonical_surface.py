from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_canonical_surface_files_exist():
    required = [
        "README.md",
        "STATUS.md",
        "FREEZE.md",
        "CITATION.cff",
        ".github/workflows/canonical-surface.yml",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), f"missing canonical surface file: {rel}"

def test_readme_identifies_template_scope():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "template" in text.lower()
    assert "urf" in text.lower()

def test_status_and_freeze_are_repo_scope():
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    freeze = (ROOT / "FREEZE.md").read_text(encoding="utf-8")
    assert "repository" in status.lower()
    assert "template" in status.lower()
    assert "canonical" in status.lower()
    assert "canonical template" in freeze.lower() or "canonical" in freeze.lower()
