"""Sphinx configuration."""
project = "Bourbaki.Types"
author = "Matt Hawthorn"
copyright = "2023, Matt Hawthorn"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
