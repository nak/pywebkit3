#!/usr/bin/python
from setuptools import setup, find_packages

setup( name = "PyGGI",
    version = "0.9.20",
    packages = ["pyggi","pyggi/javascript"],# find_packages(),
    scripts = [],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3'],
    package_data={ 'pyggi': ['lib/Windows/*']},

    include_package_data = True,
    exclude_package_data = {'':[]},
    # metadata for upload to PyPI
    author = "John Rusnak",
    author_email = "john.j.rusnak@att.net",
    description = "A binding for webkitgtk and gtk (gdk,...)",
    license = "LGPL",
    keywords = "webkit python pywebkit gtk binding",
    url = "http://github.com/nak/pyggi",   # project home page, if any

    #entry_points = { 'console_scripts': []},
    #dependency_links = []

    # could also include long_description, download_url, classifiers, etc.
)
