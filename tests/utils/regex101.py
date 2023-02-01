"""This modules contains a Regex101 regex for tests purpouses."""

import re
from typing import List


def get_url(web_app_url: str):
    """
    Transform URL from Regex101 Web App to Regex101 API.

    :param web_app_url: web app url to convert
    :type web_url: str
    """
    web_app_regex = r".*/r/(\w+)/(\d+)"
    if not re.match(web_app_regex, web_app_url):
        raise ValueError("web_app_url doesn't match valid regex")

    api_url_repl = r"https://regex101.com/api/regex/\g<1>/\g<2>"
    return re.sub(web_app_regex, api_url_repl, web_app_url)


def escape(string: str):
    """Replicate the escaping made by Regex101 API."""
    return string.translate(str.maketrans({"\n": "\\n"}))


class UnitTest:
    """A self-contained unit tests from remote store."""

    description: str
    criteria: str
    target: str
    test_string: str
    compare_string: None

    def __init__(
        self,
        description: str,
        criteria: str,
        target: str,
        test_string: str,
        compare_string: None,
    ) -> None:
        """Instance a new Unit Tests."""
        self.description = description
        self.criteria = criteria
        self.target = target
        self.test_string = test_string
        self.compare_string = compare_string


class Regex101:
    """A Regex from remote store."""

    regex: str
    test_string: str
    flags: str
    delimiter: str
    flavor: str
    substitution: None
    title: None
    unit_tests: List[UnitTest]
    is_favorite: bool
    is_library_entry: bool

    def __init__(
        self,
        regex: str,
        flags: str,
        delimiter: str,
        flavor: str,
        substitution: None,
        title: None,
        test_string: str = "",
        unit_tests: List[UnitTest] = [],
        is_favorite: bool = False,
        is_library_entry: bool = False,
        **kwargs
    ) -> None:
        """Instance a new Regex."""
        self.regex = regex
        self.test_string = (
            kwargs.get("testString", "") if not test_string else test_string
        )
        self.flags = flags
        self.delimiter = delimiter
        self.flavor = flavor
        self.substitution = substitution
        self.title = title
        unit_test_instances = [isinstance(x, UnitTest) for x in unit_tests].count(
            False
        ) == 0
        self.unit_tests = (
            [UnitTest(**x) for x in unit_tests] if unit_test_instances else unit_tests
        )
        self.is_favorite = (
            kwargs.get("isFavorite", "") if not is_favorite else is_favorite
        )
        self.is_library_entry = (
            kwargs.get("isLibraryEntry", "")
            if not is_library_entry
            else is_library_entry
        )
