from check_io import result_matches_expected

from sorting import sort_by_max_sublist_length
from sorting import sort_evenly_given_sublist_count


def test_even_sorting_happy_path():
    sublist_count = 5
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [[1, 6], [2, 7], [3, 8], [4, 9], [5, 10]]
    result = sort_evenly_given_sublist_count(sublist_count, input)
    assert result_matches_expected(result, expected)

    sublist_count = 5
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1, 6, 11], [2, 7], [3, 8], [4, 9], [5, 10]]
    result = sort_evenly_given_sublist_count(sublist_count, input)
    assert result_matches_expected(result, expected)

    sublist_count = 11
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
    result = sort_evenly_given_sublist_count(sublist_count, input)
    assert result_matches_expected(result, expected)

    sublist_count = 1
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    result = sort_evenly_given_sublist_count(sublist_count, input)
    assert result_matches_expected(result, expected)

    sublist_count = 2
    input = ["non", "numeric", "input", "list"]
    expected = [["non", "input"], ["numeric", "list"]]
    result = sort_evenly_given_sublist_count(sublist_count, input)
    assert result_matches_expected(result, expected)

    sublist_count = 3
    input = [["input", "made"], ["up"], ["of", "list"], ["of", "lists"]]
    expected = [
        [["input", "made"], ["of", "lists"]],
        [["up"]],
        [["of", "list"]],
    ]
    result = sort_evenly_given_sublist_count(sublist_count, input)
    assert result_matches_expected(result, expected)


def test_uneven_sorting_happy_path():
    # even_sorting = False - so max_sublist_length should be reached
    even_sorting = False

    max_per_sublist = 8
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11]]
    result = sort_by_max_sublist_length(max_per_sublist, input, even_sorting)
    assert result_matches_expected(result, expected)

    max_per_sublist = 3
    input = ["non", "numeric", "input", "list"]
    expected = [["non", "numeric", "input"], ["list"]]
    result = sort_by_max_sublist_length(max_per_sublist, input, even_sorting)
    assert result_matches_expected(result, expected)

    max_per_sublist = 3
    input = [["input", "made"], ["up"], ["of", "list"], ["of", "lists"]]
    expected = [[["input", "made"], ["up"], ["of", "list"]], [["of", "lists"]]]
    result = sort_by_max_sublist_length(max_per_sublist, input, even_sorting)
    assert result_matches_expected(result, expected)

    # even_sorting = True
    # max_sublist_length should will only be reached if input length / max_sublist_length is even number
    even_sorting = True

    max_per_sublist = 8
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10]]
    result = sort_by_max_sublist_length(max_per_sublist, input, even_sorting)
    assert result_matches_expected(result, expected)

    max_per_sublist = 3
    input = ["non", "numeric", "input", "list"]
    expected = [["non", "input"], ["numeric", "list"]]
    result = sort_by_max_sublist_length(max_per_sublist, input, even_sorting)
    assert result_matches_expected(result, expected)

    max_per_sublist = 3
    input = [["input", "made"], ["up"], ["of", "list"], ["of", "lists"]]
    expected = [[["input", "made"], ["of", "list"]], [["up"], ["of", "lists"]]]
    result = sort_by_max_sublist_length(max_per_sublist, input, even_sorting)
    assert result_matches_expected(result, expected)

    # even_sorting = True / False yiels the same result
    even_sorting = [True, False]
    for sorting_preference in even_sorting:
        max_per_sublist = 11
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
        result = sort_by_max_sublist_length(
            max_per_sublist, input, sorting_preference
        )
        assert result_matches_expected(result, expected)

        max_per_sublist = 1
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
        result = sort_by_max_sublist_length(
            max_per_sublist, input, sorting_preference
        )
        assert result_matches_expected(result, expected)


def test_even_sorting_non_happy_path():
    expected = "invalid input"

    sublist_count = 0
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        sort_evenly_given_sublist_count(sublist_count, input)
    except Exception as e:
        assert result_matches_expected(e, expected)

    sublist_count = 11
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        sort_evenly_given_sublist_count(sublist_count, input)
    except Exception as e:
        assert result_matches_expected(e, expected)

    sublist_count = "not an integer"
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        sort_evenly_given_sublist_count(sublist_count, input)
    except Exception as e:
        assert result_matches_expected(e, expected)

    sublist_count = -1
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        sort_evenly_given_sublist_count(sublist_count, input)
    except Exception as e:
        assert result_matches_expected(e, expected)

    sublist_count = 2
    input = "input is not a list"
    try:
        sort_evenly_given_sublist_count(sublist_count, input)
    except Exception as e:
        assert result_matches_expected(e, expected)


def test_uneven_sorting_non_happy_path():
    expected = "invalid input"

    even_sorting = [True, False]
    for sorting_preference in even_sorting:
        max_per_sublist = 0
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        try:
            sort_by_max_sublist_length(
                max_per_sublist, input, sorting_preference
            )
        except Exception as e:
            assert result_matches_expected(e, expected)

        max_per_sublist = 12
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        try:
            sort_by_max_sublist_length(
                max_per_sublist, input, sorting_preference
            )
        except Exception as e:
            assert result_matches_expected(e, expected)

        max_per_sublist = "not an integer"
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        try:
            sort_by_max_sublist_length(
                max_per_sublist, input, sorting_preference
            )
        except Exception as e:
            assert result_matches_expected(e, expected)

        max_per_sublist = -1
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        try:
            sort_by_max_sublist_length(
                max_per_sublist, input, sorting_preference
            )
        except Exception as e:
            assert result_matches_expected(e, expected)

        max_per_sublist = 3
        input = "input is not a list "
        try:
            sort_by_max_sublist_length(
                max_per_sublist, input, sorting_preference
            )
        except Exception as e:
            assert result_matches_expected(e, expected)

    even_sorting = "Not true or false"
    expected = (
        "even_sorting must be True or False, instead found: Not true or false"
    )
    max_per_sublist = 1
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    try:
        sort_by_max_sublist_length(max_per_sublist, input, even_sorting)
    except Exception as e:
        assert result_matches_expected(e, expected)


test_even_sorting_happy_path()
test_uneven_sorting_happy_path()
test_even_sorting_non_happy_path()
test_uneven_sorting_non_happy_path()
