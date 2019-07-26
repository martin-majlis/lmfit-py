# lmfit documentation build configuration file
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import date
import os
import sys

import lmfit

# -------------------------- General configuration --------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath(os.path.join('.')))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

# we want to swap sphinx.ext.mathjax and sphinx.ext.pngmath depending on the
# type of documentation we build
from extensions import extensions

# shpinx.ext.napoleon settings
napoleon_google_docstring = False

# shpinx.ext.autodoc settings
autoclass_content = 'both'

# shpinx.ext.intersphinx settings
intersphinx_mapping = {'py': ('https://docs.python.org/3', None),
                       'numpy': ('https://docs.scipy.org/doc/numpy/', None),
                       'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
                       }

# shpinx.ext.extlinks settings
extlinks = {
    'scipydoc': ('https://docs.scipy.org/doc/scipy/reference/generated/scipy.%s.html', 'scipy.'),
    'numpydoc': ('https://docs.scipy.org/doc/numpy/reference/generated/numpy.%s.html', 'numpy.'),
    }

# sphinx.ext.imgmath settings
imgmath_image_format = 'svg'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = {'.rst': 'restructuredtext'}

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'lmfit'
copyright = u'{}, Matthew Newville, Till Stensitzki, and others'.format(date.today().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
version = release = lmfit.__version__.split('+', 1)[0]

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['sphinx/theme']
html_theme = 'lmfitdoc'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Non-Linear Least-Squares Minimization and Curve-Fitting for Python'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Minimization and Curve-Fitting for Python'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}

html_domain_indices = False
html_use_index = True
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'lmfitdoc'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'lmfit.tex',
   'Non-Linear Least-Squares Minimization and Curve-Fitting for Python',
   'Matthew Newville, Till Stensitzki, and others', 'manual'),
]

# configuration for jupyter_sphinx
package_path = os.path.abspath('../..')
os.environ['PYTHONPATH'] = ':'.join((package_path, os.environ.get('PYTHONPATH', '')))

image_converter_args=["-density", "300"]
