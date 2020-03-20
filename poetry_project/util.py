from pathlib import Path
import tomlkit


def load_pyproject_toml(base_path, file_name='pyproject.toml'):
    d = Path(base_path)

    while d.parent != d:
        d = d.parent
        pyproject_path = Path(d, file_name)
        if pyproject_path.exists():
            with open(file=str(pyproject_path)) as handle:
                return tomlkit.parse(string=handle.read())
    return None


def get_poetry_attribute(attribute_name, base_path=__file__, pyproject_toml=None):
    if pyproject_toml is None:
        pyproject_toml = load_pyproject_toml(base_path)

    if 'tool' not in pyproject_toml or 'poetry' not in pyproject_toml['tool']:
        return None

    attribute_path = attribute_name.split('.')
    unwrapped = pyproject_toml['tool']['poetry']
    for attribute in attribute_path:
        if attribute not in unwrapped:
            return None
        unwrapped = unwrapped[attribute]
    return unwrapped
