import setuptools

# https://packaging.python.org/guides/single-sourcing-package-version/

import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as fh:
    long_description = fh.read()

test_deps = [
    'pytest',
    'pytest-cov',
    'pytest-pycodestyle',
    'pytest-pep8',
    'pytest-flake8',
]

extras = {
    'test': test_deps,
}

description = """
markdown-sql-eval takes a markdown-formatted input and executes the sql queries
found in it, and returns a markdown-formatted output where the results of the
sql queries have been added. markdown-sql-eval comes with a command line tool
with a same name which can be used to process markdown files. Project is
developed and hosted in GitHub: https://github.com/ahojukka5/gmshparser.
"""

entry_points = {
    'console_scripts': ['markdown-sql-eval=markdown_sql_eval.cli:main'],
}

setuptools.setup(
    name="markdown_sql_eval",
    version=get_version("markdown_sql_eval/__init__.py"),
    author="Jukka Aho",
    author_email="ahojukka5@gmail.com",
    description=" ".join(description.strip().splitlines()),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahojukka5/markdown-sql-eval",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    tests_require=test_deps,
    extras_require=extras,
    entry_points=entry_points,
)
