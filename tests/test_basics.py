import poetry_project
from poetry_project import get_version, get_name
from poetry_project.util import load_pyproject_toml, load_toml_from_package


def test_load_own_package_not_none():
    toml_object = load_toml_from_package(poetry_project)

    assert toml_object is not None


def test_load_own_version():
    version = get_version(poetry_project)

    assert version is not None
    assert len(version) > 1


def test_load_not_none():
    toml_object = load_pyproject_toml(base_path=__file__)

    assert toml_object is not None


def test_load_version_default():
    version = get_version()

    assert version is not None
    assert len(version) > 1


def test_load_name_default():
    version = get_name()

    assert version is not None
    assert len(version) > 1

