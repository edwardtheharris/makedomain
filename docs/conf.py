# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import pathlib

author = 'Kay-Uwe Lorenz'
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
    'myst_parser',
    'sphinx.ext.autodoc',
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
