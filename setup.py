from setuptools import setup

setup(
    name = "Markdown Inline Graphviz Extension",
    version = "1.0",
    py_modules = ["mdx_inline_graphviz"],
    install_requires = ['Markdown>=2.3.1'],
    author = "Steffen Prince",
    author_email = "steffen@sprin.io",
    description = "Render inline graphs with Markdown and Graphviz",
    license = "MIT",
    url = "https://github.com/sprin/markdown-inline-graphviz",
)
