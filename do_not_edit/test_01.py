import ...task_01

def test_task_01():
    """
    Test that Task 01 is completed.

    By this stage, students need to have created a 2D list. The inner lists
    will each contain seven strings.
    """
    # Check that `days` is a list of lists of strings.
    valid_type = isinstance(task_01.days, list[list[str]])

    # Check that there are three inner lists.
    valid_count = len(task_01.days) == 3

    # Check that there are seven items in each of the inner lists.
    valid_inner_count = all([len(lang) == 7 for lang in task_01.days])

    # Assert that all the tests are True.
    assert all(valid_type, valid_count, valid_inner_count)