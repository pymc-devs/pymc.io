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
from pathlib import Path


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
    "jupyterlite_sphinx",
    "sphinxext.rediraffe",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

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
    "arviz": ("https://python.arviz.org/en/latest/", None),
    "bambi": ("https://bambinos.github.io/bambi/main", None),
    "mpl": ("https://matplotlib.org/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pymc": ("https://www.pymc.io/projects/docs/en/stable/", None),
    "nb": ("https://www.pymc.io/projects/examples/en/latest/", None),
    "pmx": ("https://www.pymc.io/projects/experimental/en/latest/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "xarray": ("https://docs.xarray.dev/en/stable/", None),
}

blog_baseurl = "https://pymc.io"
blog_title = "PyMC project website"
blog_path = "blog"
blog_authors = {
    "contributors": ("PyMC Contributors", "https://pymc.io"),
    "oriol": ("Oriol Abril Pla", "https://oriolabril.github.io"),
}
blog_default_author = "contributors"
fontawesome_included = True

notfound_urls_prefix = ""

rediraffe_redirects = {
    "index.md": "welcome.md",
}

def remove_catalogs(app):
    """
    This removes the tag, category and archive pages so ablog rewrites them.
    They need to be present initially for the toctree and sidebar to work.
    """

    app.env.project.docnames -= {"blog/tag", "blog/category", "blog/archive"}
    yield "blog", {}, "layout.html"

def remove_index(app):
    """
    This removes the index pages so rediraffe generates the redirect placeholder
    It needs to be present initially for the toctree as it defines the navbar.
    """

    index_file = Path(app.outdir) / "index.html"
    index_file.unlink()

    app.env.project.docnames -= {"index"}
    yield "", {}, "layout.html"


def setup(app):
    """
    Add extra steps to sphinx build
    """

    app.connect("html-collect-pages", remove_catalogs, 100)
    app.connect("html-collect-pages", remove_index, 100)

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
html_theme = "pydata_sphinx_theme"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pymc-devs/pymc",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/pymc_devs",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/c/PyMCDevelopers",
            "icon": "fab fa-youtube",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.pymc.io",
            "icon": "fab fa-discourse",
        },
    ],
    "use_edit_page_button": True,
    "navbar_end": ["search-field.html", "navbar-icon-links.html"],
    "page_sidebar_items": ["page-toc", "edit-this-page", "donate"],
    "search_bar_text": "Search...",
    "show_nav_level": 2,
}
html_context = {
    "github_user": "pymc-devs",
    "github_repo": "pymc.io",
    "github_version": "main",
    "doc_path": ".",
}

html_logo = "_static/PyMC.jpg"
html_favicon = "_static/favicon.ico"

html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "PyMC project website"

html_sidebars = {
    "blog/tag": [
        "tagcloud.html",
        "sidebar-nav-bs.html",
    ],
    "blog/category": [
        "categories.html",
        "sidebar-nav-bs.html",
    ],
    "blog/archive": [
        "archives.html",
        "sidebar-nav-bs.html",
    ],
    "blog/*": [
        "postcard.html",
        "sidebar-nav-bs.html",
    ],
    "blog": ["sidebar-nav-bs.html"],
    "[!blog]**": ["sidebar-nav-bs.html"],
}
