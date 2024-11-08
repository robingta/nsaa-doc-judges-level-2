"""Sphinx configuration file."""

from __future__ import annotations

import os
from dataclasses import asdict

from dotenv import load_dotenv
from sphinx.application import Sphinx
from sphinx.util.docfields import Field
from sphinxawesome_theme import ThemeOptions, __version__
from sphinxawesome_theme.postprocess import Icons

load_dotenv()

# -- Project information ---

project = "NSAA Judges"
author = "Critical It Group"
copyright = f"{author}."

# -- General configuration ---

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx_sitemap",
    "sphinx_design",
    "sphinx_docsearch",
    "sphinxcontrib.images",
]

exclude_patterns = ["public", "includes", "**/includes"]

nitpicky = True

default_role = "literal"

# Global substitutions for reStructuredText files
substitutions = [
    ":tocdepth: 3",
    " ",
    ".. meta::",
    "   :author: kai687",
    "   :keywords: Documentation,Sphinx,Python,Tailwind",
    ".. |rst| replace:: reStructuredText",
    ".. |product| replace:: Awesome Theme",
    ".. |conf| replace:: File: conf.py",
    f".. |current| replace:: {__version__}",
]
rst_prolog = "\n".join(substitutions)

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

extlinks = {
    "gh": ("https://github.com/kai687/sphinxawesome-theme/blob/main/%s", "%s"),
    "ghdir": ("https://github.com/kai687/sphinxawesome-theme/tree/main/%s", "%s"),
    "sphinxdocs": ("https://www.sphinx-doc.org/en/master/%s", "%s"),
}

add_module_names = False

# -- Options for HTML output ---
html_show_sphinx = False
html_title = project
html_theme = "sphinxawesome_theme"
html_last_updated_fmt = ""
html_use_index = False  # Don't create index
html_domain_indices = False  # Don't need module indices
html_copy_source = False  # Don't need sources
html_logo = "./images/logo/logo.png"
html_favicon = "./images/logo/logo.png"
html_permalinks_icon = Icons.permalinks_icon
html_baseurl = "https://sphinxawesome.xyz/"
html_extra_path = []
html_context = {
    "mode": "production",
    "feedback_url": "https://github.com/kai687/sphinxawesome-theme/issues/new?title=Feedback",
    "umami_website_id": os.getenv("UMAMI_WEBSITE_ID", ""),
}

html_sidebars: dict[str, list[str]] = {
    "about": ["sidebar_main_nav_links.html"],
}

# if you want to include other pages than docs
templates_path = ["_templates"]
# html_additional_pages = {"about": "about.html"}

html_static_path = ["_static"]
html_css_files = ["feedback.css"]
html_js_files = [("feedback.js", {"defer": "defer"})]

# DocSearch
docsearch_app_id = os.getenv("DOCSEARCH_APP_ID", "")
docsearch_api_key = os.getenv("DOCSEARCH_API_KEY", "")
docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME", "")
docsearch_placeholder = "Search these docs"
docsearch_missing_results_url = (
    "https://github.com/kai687/sphinxawesome-theme/issues/new?title=${query}"
)

theme_options = ThemeOptions(
    show_prev_next=True,
    awesome_external_links=True,
    main_nav_links={

    },
    extra_header_link_icons={
           
    },
)

html_theme_options = asdict(theme_options)

sitemap_url_scheme = "{link}"


# -- Register a :confval: interpreted text role ----------------------------------
def setup(app: Sphinx) -> None:
    """Register the ``confval`` role and directive.

    This allows to declare theme options as their own object
    for styling and cross-referencing.
    """
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration parameter",
        doc_field_types=[
            Field(
                "default",
                label="default",
                has_arg=True,
                names=("default",),
                bodyrolename="class",
            )
        ],
    )
