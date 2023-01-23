# Getting Started

## How to Install

Use pip to install the plugin (or use your preferred dep manager for Python, like [Poetry](https://python-poetry.org/) for me):

    pip install mkdocs-bulma-classes-plugin

## How to use

Activate the plugin in your `mkdocs.yml` config file:

    plugins:
      - bulma-classes

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

You doesn't need to do anything. When you build your docs with Mkdocs, after HTML page generation, this pluging inject in your tags the proper CSS class for Bulma. For example, your `# Heading 1` will produce the following HTML code:

    <h1 id="heading-1">Heading 1</h1>

but enabling this plugin will produce this:

    <h1 id="heading-1" class="title is-1">Heading 1</h1>

necessary for Bulma to render this title:

![Bulma title is-1](img/bulma_heading_1.png)

For more info, look at [docs](https://daniele-tentoni.github.io/mkdocs-bulma-classes-plugin).
