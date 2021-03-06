"""
author: Zoran Simic zoran@simicweb.com      # will be auto-adjusted
url: https://github.com/zsimic              # url will be auto-completed
download_url: archive/{version}.tar.gz      # will be auto-completed too
keywords: setup, docstring
version: 1.0a1
"""

from setuptools import setup


__version__ = "1.0b1"
__keywords__ = "some,list,of,keywords,here,long,enough,to,be,abbreviated,by,the,explain,command"

setup(
    name="complex",
    versioning="distance;.hooks/bump",
    setup_requires=["setupmeta"],
    # This will overshadow classifiers.txt
    classifiers=["Programming Language :: Python"],

    extras_require=dict(
        bar=["docutils"],
        baz=["some", "long", "list-of", "requirements"],
        foo=["long", "enough", "to-be", "abbreviated"],
    ),

    # Edge case galore
    keywords=__keywords__.split(","),
    entry_points=dict(console_scripts="a=b"),
    license="foo",
)
