import sys

# This lets the test import from the root directory.
sys.path.append("..")

import task_03


def test_task_03_valid_type():
    # Check that `lang_names` is a list of strings.
    assert isinstance(task_03.lang_names, list)


def test_task_03_valid_inner_list_types():
    # Check that all the inner items are strings.
    assert all([isinstance(lang, str) for lang in task_03.lang_names])


def test_task_03_valid_inner_list_count():
    # Check that there are four strings for the names of the languages.
    assert len(task_03.lang_names) == 4
