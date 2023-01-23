import re
from typing import Optional
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page


class BulmaClassesPlugin(BasePlugin):
    config_scheme = {
        ("param", config_options.Type(str, default="")),
    }

    markdown_regexes = {
        "(.*)\n(=+)(\n+)(.*)\n(-+)": '<h1 class="title is-1 has-text-light" id="\g<1>">\g<1></h1><h3 class="subtitle is-3 has-text-light" id="\g<4>">\g<4></h3>'
    }

    regex_dict = {
        "<table>": '<table class="table">',
        "<h1 id=\"(.*)\">": '<h1 id=\"\g<1>\" class="title is-1 has-text-light">',
        "<h2 id=\"(.*)\">": '<h2 id=\"\g<1>\" class="title is-2 has-text-light">',
        "<h3 id=\"(.*)\">": '<h3 id=\"\g<1>\" class="title is-3 has-text-light">',
        "<h4 id=\"(.*)\">": '<h4 id=\"\g<1>\" class="title is-4 has-text-light">',
        "<h5 id=\"(.*)\">": '<h5 id=\"\g<1>\" class="title is-5 has-text-light">',
        "<h6 id=\"(.*)\">": '<h6 id=\"\g<1>\" class="title is-6 has-text-light">',
    }

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_page_markdown(
        self, markdown: str, page: Page, config, files
    ) -> Optional[str]:
        # Substitute any element that need Markdown to be mapped.
        for key, value in self.markdown_regexes.items():
            regex = re.compile(key, re.MULTILINE)
            # TODO: This substitution not leave any chance to process any
            # markdown inside a captured content of the regex (.*), like the
            # issue with Titles and Subtitles. There's a possibility to make it
            # with the least possible complexity?
            markdown = re.sub(regex, value, markdown)

        return markdown

    def on_post_page(self, output: str, *, page: Page, config) -> Optional[str]:
        # Substitute any element that need HTML to be mapped.
        # Here we take all other simple Markdown elements with easy mapping to Bulma classes
        for key, value in self.regex_dict.items():
            output = re.sub(re.compile(key), value, output)
        return output
