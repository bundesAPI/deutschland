import pytest


def test_all_imports():
    pass


def test_package_imports():
    pass


def test_failing_imports():
    with pytest.raises(ImportError, match="cannot import name 'GibtsJaGarNicht'"):
        pass
