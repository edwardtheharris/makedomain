# -*- coding: utf-8 -*-
"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""
import pathlib

author = 'Kay-Uwe Lorenz'
autodoc2_docstring_parser_regexes = [
    # this will render all docstrings as Markdown
    (r".*", "myst"),
]
autodoc2_packages = [
    {
        'path': '../sphinxcontrib',
        'auto_mode': False,
    }
]
autodoc2_render_plugin = 'myst'
copyright = '2023, Kay-Uwe Lorenz'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
exclude_patterns = [
    '_build',
    '.DS_Store',
    '.venv',
    'Thumbs.db',
]

extensions = [
    'autodoc2',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx.ext.githubpages',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

myst_title_to_header = True
project = 'Sphinx Contribution Make Domain'
with pathlib.Path('../version').open('r', encoding='utf-8') as r_fh:
    release = r_fh.read()
show_authors = True
templates_path = ['_templates']
