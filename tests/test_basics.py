import poetry_project
import tomlkit
import pathlib
from poetry_project import get_version, get_name, get_dependencies
from poetry_project.util import load_toml_from_package


def test_load_own_package_not_none():
    toml_object = load_toml_from_package(poetry_project)

    assert toml_object is not None


def test_load_own_version():
    version = get_version(poetry_project)

    assert version is not None
    assert len(version) > 1


def test_load_version_default():
    version = get_version()

    assert version is not None
    assert len(version) > 1


def test_load_name_default():
    version = get_name()

    assert version is not None
    assert len(version) > 1


def test_this_version_matches_project_file():
    # Arrange
    project_file = pathlib.Path('../pyproject.toml')
    current_toml_content = tomlkit.parse(project_file.read_text())
    current_version = current_toml_content['tool']['poetry']['version']

    # Act
    version = get_version()

    assert version is not None
    assert len(version) > 1
    assert version == current_version


def test_get_version_falls_back_to_importlib():
    # Act
    tomlkit_version = get_version('tomlkit')

    # Assert
    assert tomlkit_version is not None
    assert len(tomlkit_version) > 1


def test_get_dependencies_not_empty():
    # Act
    deps = get_dependencies()

    # Assert
    assert len(deps) > 0

