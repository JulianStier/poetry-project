# poetry-project
Load pyproject.toml information into your project.

From Pypi:
``pip install poetry_project``

Usage:
```python
from poetry_project import get_version
__version__ = get_version('your_package_name')
```
or:
```python
import your_package  # must contain a pyproject.toml
from poetry_project import get_version
__version__ = get_version('your_package')
```

**Importantly** note, that you need to ship your *pyproject.toml* explicitly to your package.
This requires additional configuration, e.g. by adding the file to the include-statement within your *pyproject.toml*:
```toml
[tool.poetry]
include = [
    "pyproject.toml"
]
```
Only then gets this file actually packaged when delivered e.g. by PyPi.

# Development

## Deployment to PyPi
``poetry build``
``twine upload dist/*``