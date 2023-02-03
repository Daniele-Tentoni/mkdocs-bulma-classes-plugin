import re

import pytest
from mkdocs_bulma_classes_plugin.regexs.regex import Regex


@pytest.fixture(name="regex")
def base_regex() -> Regex:
    return Regex(r"regex(.*)inside", r"regex\g<1>outside", re.MULTILINE)


@pytest.mark.parametrize(
    ["string", "result"],
    [("regex outside", False), ("regex inside", True), ("regex far away inside", True)],
)
def test_regex_search(string, result, regex: Regex):
    found = regex.search(string) is not None
    assert found == result


@pytest.mark.parametrize(
    ["string", "result"],
    [
        ("regex outside", "regex outside"),
        ("regex inside", "regex outside"),
        ("regex far away inside", "regex far away outside"),
    ],
)
def test_regex_sub(string, result, regex: Regex):
    substituted = regex.sub(string)
    assert substituted == result
