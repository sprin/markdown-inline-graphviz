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
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Documentation',
        'Topic :: Text Processing',

        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
