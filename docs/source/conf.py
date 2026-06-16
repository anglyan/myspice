import os
import sys
from importlib.metadata import version as get_version

sys.path.insert(0, os.path.abspath("../../src"))

project = "myspice"
copyright = "2026, Angel Yanguas"
author = "Angel Yanguas"
release = get_version("myspice")
version = ".".join(release.split(".")[:2])

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
