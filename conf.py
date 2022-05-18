# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "PyMC project website"
copyright = "2022, PyMC Team"
author = "PyMC Team"
version = ""
release = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
    "ablog",
    "sphinxext.opengraph",
    "sphinx_codeautolink",
    "notfound.extension",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    ".ipynb_checkpoints",
    "_build",
    "jupyter_execute",
    "README.md",
]

# -- Options for extensions

jupyter_execute_notebooks = "auto"
execution_excludepatterns = ["*.ipynb"]
myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath"]

intersphinx_mapping = {
    "aesara": ("https://aesara.readthedocs.io/en/latest/", None),
    "arviz": ("https://arviz-devs.github.io/arviz", None),
    "bambi": ("https://bambinos.github.io/bambi/main", None),
    "mpl": ("https://matplotlib.org/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pymc": ("https://docs.pymc.io/en/stable", None),
    "nb": ("https://docs.pymc.io/projects/examples/en/latest/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "xarray": ("https://xarray.pydata.org/en/stable/", None),
}

blog_baseurl = "https://pymc.io"
blog_title = "Keeping up with PyMC"
blog_path = "blog"
blog_authors = {
    "contributors": ("PyMC Contributors", "https://pymc.io"),
    "oriol": ("Oriol Abril Pla", "https://oriolabril.github.io"),
}
blog_default_author = "contributors"
fontawesome_included = True

ogp_site_url = "https://pymc.io"
ogp_image = "https://pymc.io/_static/PyMC.jpg"
ogp_use_first_image = True

ogp_custom_meta_tags = [
    # TODO: add fancy twitter specific metadata
    # '<meta property="og:ignore_canonical" content="true" />',
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_theme_options = {
    "repository_url": "https://github.com/pymc-devs/pymc.io",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": False,
    "logo_only": True,
    "search_bar_text": "Search...",
}

html_logo = "_static/PyMC.jpg"
html_favicon = "_static/favicon.ico"

html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "Keeping up with PyMC"

html_sidebars = {
    "blog/tag": [
        "sidebar-logo.html",
        "search-field.html",
        "tagcloud.html",
        "sbt-sidebar-nav.html",
    ],
    "blog/category": [
        "sidebar-logo.html",
        "search-field.html",
        "categories.html",
        "sbt-sidebar-nav.html",
    ],
    "blog/archive": [
        "sidebar-logo.html",
        "search-field.html",
        "archives.html",
        "sbt-sidebar-nav.html",
    ],
    "blog/*": [
        "sidebar-logo.html",
        "search-field.html",
        "postcard.html",
        "sbt-sidebar-nav.html",
    ],
    "blog": [
        "sidebar-logo.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
    ],
    "[!blog]**": [
        "sidebar-logo.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
    ]
}
