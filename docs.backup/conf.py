# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BlueROV Guide'
copyright = '2025, Francisco Javier Bellas Bouza, Félix Orjales Saavedra, Bakel Bakel, GII'
author = 'Francisco Javier Bellas Bouza, Félix Orjales Saavedra, Bakel Bakel, GII'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


html_baseurl = 'https://bakel-bakel.github.io/blueROV-guide/'

html_theme_options = {
    'navigation_with_keys': True  # optional
}

