import pytest
from mkdocs_bulma_classes_plugin.plugin import BulmaClassesPlugin


@pytest.fixture(name="plugin")
def base_plugin() -> BulmaClassesPlugin:
    return BulmaClassesPlugin()


def test_plugin_creation(plugin: BulmaClassesPlugin):
    assert plugin.enabled == True


def test_on_page_markdown(plugin: BulmaClassesPlugin):
    markdown_that_doesnt_change = "# Title"
    markdown = plugin.on_page_markdown(markdown_that_doesnt_change, None, None, None)
    assert markdown == markdown_that_doesnt_change


def test_on_post_page(plugin: BulmaClassesPlugin):
    html_that_doesnt_change = "<p>HTML</p>"
    html = plugin.on_post_page(html_that_doesnt_change, page=None, config=None)
    assert html == html_that_doesnt_change
