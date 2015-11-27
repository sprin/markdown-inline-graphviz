Markdown Inline Graphviz
========================

A Python Markdown extension that replaces inline dot graphs with inline SVGs
or PNGs!

Why render the graphs inline? No configuration! Works with any
Python-Markdown-based static site generator, such as
[MkDocs](http://www.mkdocs.org/), [Pelican](http://blog.getpelican.com/), and
[Nikola](https://getnikola.com/) out of the box without configuring an output
directory.

# Installation

    $ pip install markdown-inline-graphviz

# Usage

Activate the `inline_graphviz` extension. For example, with Mkdocs, you add a
stanza to mkdocs.yml:

```
markdown_extensions:
    - inline_graphviz
```

To use it in your Markdown doc:

```
{% dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
%}
```

# Credits

Inspired by [jawher/markdown-dot](https://github.com/jawher/markdown-dot),
which renders the dot graph to a file instead of inline.


# License

[MIT License](http://www.opensource.org/licenses/mit-license.php)
