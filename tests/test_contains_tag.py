# -*- coding: utf-8 -*-
import pathlib

import cachedir_tag


# A regular file starting with the expected header should return True


def test_file_exact(tmp_path: pathlib.Path):
    (tmp_path / 'CACHEDIR.TAG').write_text('Signature: 8a477f597d28d172789f06886806bc55')
    assert cachedir_tag.contains_tag(tmp_path) == True


def test_file_with_trailing(tmp_path: pathlib.Path):
    (tmp_path / 'CACHEDIR.TAG').write_text('Signature: 8a477f597d28d172789f06886806bc55extendededition')
    assert cachedir_tag.contains_tag(tmp_path) == True


# Everything else should return False


def test_file_with_leading(tmp_path: pathlib.Path):
    (tmp_path / 'CACHEDIR.TAG').write_text('\nSignature: 8a477f597d28d172789f06886806bc55')
    assert cachedir_tag.contains_tag(tmp_path) == False


def test_file_truncated(tmp_path: pathlib.Path):
    (tmp_path / 'CACHEDIR.TAG').write_text('Signature: 8a477f597d28d172789f06')
    assert cachedir_tag.contains_tag(tmp_path) == False


def test_absent(tmp_path: pathlib.Path):
    assert cachedir_tag.contains_tag(tmp_path) == False


def test_directory(tmp_path: pathlib.Path):
    (tmp_path / 'CACHEDIR.TAG').mkdir()
    assert cachedir_tag.contains_tag(tmp_path) == False


def test_symlink(tmp_path: pathlib.Path):
    (tmp_path / 'foo.txt').write_text('Signature: 8a477f597d28d172789f06886806bc55')
    (tmp_path / 'CACHEDIR.TAG').symlink_to('foo.txt')
    assert cachedir_tag.contains_tag(tmp_path) == False
