# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MyLib'
copyright = '2024, Nicolas Gensollen'
author = 'Nicolas Gensollen'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",
    "myst_nb",
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- autoapi configuration ---------------------------------------------------
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html

autoapi_dirs = ['../src']
autoapi_root = "reference/api"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://gitlab.com/NicolasGensollen/my_lib",
    "repository_branch": "main",
    "navigation_with_keys": False,
}
html_title = "my lib documentation"
html_static_path = ['_static']
