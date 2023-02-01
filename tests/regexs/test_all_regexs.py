"""This module test every regex with each unit test on regex101.com."""

import importlib
import inspect

import pytest
import requests
from mkdocs_bulma_classes_plugin.regexs.regex import UnorderedListRegex
from tests.utils.regex101 import Regex101, escape, get_url


@pytest.fixture
def unordered_list_regex() -> UnorderedListRegex:
    """
    Return my regex object.

    :return: The regex used for unit tests.
    :rtype: UnorderedListRegex
    """
    return UnorderedListRegex()


@pytest.fixture
def regex101(request) -> Regex101:
    """Return Regex101 object."""
    marker = request.node.get_closest_marker("url")
    print("Url", marker.args[0])
    url = get_url(marker.args[0])
    j = requests.get(url).json()
    print(f"json {j}")
    return Regex101(**j)


def unordered_valid_regex(unordered_list_regex: UnorderedListRegex, regex101: Regex101):
    """Test if my regex is valid with the remote one."""
    assert regex101.regex == escape(unordered_list_regex.exp.pattern)


def unordered_testStrings(unordered_list_regex, regex101: Regex101):
    """Test my regex for each remote testString."""
    print(f"Content {regex101.test_string} {regex101.regex}")
    assert (
        unordered_list_regex.exp.match(regex101.test_string) is not None
    ), f"failed matching {unordered_list_regex.exp} and {regex101.test_string}"

    for u in enumerate(regex101.unit_tests):
        has_to_match = u.criteria == "DOES_MATCH"
        does_match = unordered_list_regex.exp.search(u["testString"]) is not None
        print(f'{u["testString"]}\n{has_to_match}: {does_match} --- \n')
        assert does_match == has_to_match, f"failed {u['description']}"


# The follow test download things from internet, don't run locally to don't slow down your development.
def test_all_regexs():
    """
    Looks for any class in the regex module and test to remote unit tests on regex101.com

    Use with caution.
    """
    # Those rows looks for any file in a given path.
    # Useful when I have regex classes in more then one file.
    # mypath = os.path.join("mkdocs_bulma_classes_plugin", "regexs")
    # onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
    # for x in onlyfiles:
    module = importlib.import_module("mkdocs_bulma_classes_plugin.regexs.regex")
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and hasattr(obj, "test_url"):
            print(f"Running tests in {obj.test_url} for: {name}:{obj.__class__}")
            t = obj.__class__
            r = obj()
            url = get_url(obj.test_url)
            j = requests.get(url).json()
            print(f"json {j}")
            regex101 = Regex101(**j)
            print(f"Content {regex101.test_string} {regex101.regex}")
            assert (
                r.exp.match(regex101.test_string) is not None
            ), f"failed matching {r.exp} and {regex101.test_string}"

            for u in enumerate(regex101.unit_tests):
                has_to_match = u.criteria == "DOES_MATCH"
                does_match = r.exp.search(u["testString"]) is not None
                print(f'{u["testString"]}\n{has_to_match}: {does_match} --- \n')
                assert does_match == has_to_match, f"failed {u['description']}"
