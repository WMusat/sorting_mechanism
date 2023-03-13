def integer_is_between_min_and_max(integer, min, max):
    if isinstance(integer, int) is False or integer < min or integer > max:
        # NOTE: print could be replaced with logger.debug in a more permanent implementation
        print(
            "Error: input must an integer between "
            + str(min)
            + " and "
            + str(max)
        )
        raise Exception("invalid input")
    else:
        return True


def input_is_non_empty_list(input_list):
    if len(input_list) == 0 or isinstance(input_list, list) is False:
        print("Error: input_list must be non-empty list")
        raise Exception("invalid input")
    else:
        return True


def result_matches_expected(result, expected_result):
    # NOTE: could use f-string for these print statements but that would necessitate the use of python3
    if str(result) != str(expected_result):
        raise Exception(
            "result did not match expected"
            + "\n Result: "
            + str(result)
            + "\n Expected result: "
            + str(expected_result)
        )
    else:
        print("Result matches expected")
        return True


def list_length_matches_expected(list_input, expected_length):
    if len(list_input) != expected_length:
        raise Exception(
            "list length did not match expected"
            + "\n Found: "
            + str(len(list_input))
            + "\n Expected length: "
            + str(expected_length)
        )
    else:
        return True


def input_is_true_or_false(input, input_name):
    if input not in [True, False]:
        raise Exception(
            str(input_name)
            + " must be True or False, instead found: "
            + str(input)
        )
    else:
        return True


def result_and_list_length_matches_expected(
    result, expected_result, expected_length
):
    assert result_matches_expected(result, expected_result)
    assert list_length_matches_expected(result, expected_length)
