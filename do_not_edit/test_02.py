import sys

# This lets the test import from the root directory.
sys.path.append("..")

import task_02


def test_task_02_valid_type():
    # Check that `days` is a list of lists of strings.
    assert isinstance(task_02.days, list)


def test_task_02_valid_inner_list_types():
    # Check that all the inner items are lists.
    assert all([isinstance(lang, list) for lang in task_02.days])


def test_task_02_valid_inner_list_count():
    # Check that there are four inner lists, including the newly-appended list.
    assert len(task_02.days) == 4


def test_task_02_valid_inner_item_types():
    # Check that the inner lists' items are all strings.
    assert all([[isinstance(day, str) for day in lang] for lang in task_02.days])


def test_task_02_valid_inner_item_count():
    # Check that there are seven items in each of the inner lists.
    assert all([len(lang) == 7 for lang in task_02.days])