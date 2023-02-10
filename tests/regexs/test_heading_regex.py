"""This module test every heading regex using parametrization provided by pytest."""

import pytest

from mkdocs_bulma_classes_plugin.regexs.regex import HeadingRegex


@pytest.mark.parametrize("size", [(1), (2), (3), (4), (5), (6)])
def test_search_each_size(size: int):
    """
    Test regex searching for each supported heading size.

    :param size: Heading size under test
    :type size: int
    """
    r = HeadingRegex(size)
    test_string = f'<h{size} id="title">Title</h{size}>'
    assert r.search(test_string) is not None


@pytest.mark.parametrize(
    "size, substituting, expected",
    [
        (
            1,
            '<h1 id="title">Title</h1>',
            '<h1 id="title" class="title is-1 has-text-light">Title</h1>',
        ),
        (
            2,
            '<h2 id="title">Title</h2>',
            '<h2 id="title" class="title is-2 has-text-light">Title</h2>',
        ),
        (
            3,
            '<h3 id="title">Title</h3>',
            '<h3 id="title" class="title is-3 has-text-light">Title</h3>',
        ),
        (
            4,
            '<h4 id="title">Title</h4>',
            '<h4 id="title" class="title is-4 has-text-light">Title</h4>',
        ),
        (
            5,
            '<h5 id="title">Title</h5>',
            '<h5 id="title" class="title is-5 has-text-light">Title</h5>',
        ),
        (
            6,
            '<h6 id="title">Title</h6>',
            '<h6 id="title" class="title is-6 has-text-light">Title</h6>',
        ),
    ],
)
def test_sub_each_size(size: int, substituting: str, expected: str):
    """
    Test regex substitution for each supported heading size.

    :param size: Heading size under test
    :type size: int
    :param substituting: String to be substituted
    :type substr: str
    :param result: Expected result
    :type result: str
    """
    assert HeadingRegex(size).sub(substituting) == expected
