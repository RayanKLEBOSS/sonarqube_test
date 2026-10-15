import hashlib
import pytest

from src.test3 import process, duplicate_one, duplicate_two


def test_process_returns_md5_hash(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)  # évite de toucher à un vrai fichier data.txt
    expected = hashlib.md5("admin123".encode()).hexdigest()
    assert process(0, 0, 0, 0, 0, 0, 0, 0) == expected


def test_process_division_by_zero(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(ZeroDivisionError):
        process(1, 2, 3, 4, 5, 6, 7, 8)


def test_process_removes_existing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data.txt").write_text("x")
    process(0, 0, 0, 0, 0, 0, 0, 0)
    assert not (tmp_path / "data.txt").exists()


def test_duplicate_one():
    assert duplicate_one(2) == [0, 3, 4, 5, 8, 7, 12, 9, 16, 11]


def test_duplicate_two():
    assert duplicate_two(2) == [0, 3, 4, 5, 8, 7, 12, 9, 16, 11]
