"""Tests Package Version Consistency."""
from pathlib import Path

import toml

from ml_forecasting_building_electricity import __version__


def test_versions_are_in_sync() -> None:
    """Checks if the pyproject.toml and package.__init__.py __version__ are in sync."""

    path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    pyproject = toml.loads(open(str(path)).read())
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    package_init_version = __version__

    assert package_init_version == pyproject_version
