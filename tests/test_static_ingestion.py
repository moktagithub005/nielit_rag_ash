from pathlib import Path

from ingestion.static_ingestion import StaticIngestionPipeline


def test_collect_supported_files(tmp_path):
    supported_file = tmp_path / "notes.txt"
    supported_file.write_text("Static knowledge base content", encoding="utf-8")

    nested_dir = tmp_path / "nested"
    nested_dir.mkdir()
    nested_supported = nested_dir / "doc.pdf"
    nested_supported.write_bytes(b"%PDF-1.4\n")

    ignored_file = tmp_path / "notes.md"
    ignored_file.write_text("Should be ignored", encoding="utf-8")

    pipeline = StaticIngestionPipeline()
    discovered_files = pipeline._collect_supported_files(tmp_path)

    assert discovered_files == [supported_file, nested_supported]
