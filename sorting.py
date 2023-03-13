import check_io as check


def create_sorted_list_and_sublists(sublist_count):
    # create the sorted_list and empty sublists

    sorted_list = []
    for i in range(sublist_count):
        sorted_list.append([])

    return sorted_list


def sort_input_evenly(sublist_count, input_to_sort):
    # sort the input as evenly as possible

    sorted_list = create_sorted_list_and_sublists(sublist_count)

    # for each item in the input_to_sort append the number to the target_list
    x = 0
    for i in input_to_sort:
        target_list = sorted_list[x]
        target_list.append(i)
        # start the count over once you reach the las sublist
        if x == sublist_count - 1:
            x = 0
        else:
            x = x + 1
    return sorted_list


def sort_input_unevenly(sublist_count, input_to_sort, max_sublist_length):
    # sort input unevenly to utilize the full max_sublist_length

    sorted_list = create_sorted_list_and_sublists(sublist_count)

    # for each sublist determine if you can use the full max_sublist_length
    x = 0
    for i in range(sublist_count):
        target_list = sorted_list[i]

        # use max_sublist_length if you still have enough input left
        if max_sublist_length <= len(input_to_sort) - x:
            target_list.extend(input_to_sort[x : x + max_sublist_length])
        else:
            # otherwise use the remainder
            target_list.extend(input_to_sort[x::])

        x = x + max_sublist_length

    return sorted_list


def sort_evenly_given_sublist_count(sublist_count, input_to_sort):
    # sort input as evenly as possible given the amount of sublists

    assert check.integer_is_between_min_and_max(
        sublist_count, 1, len(input_to_sort)
    )

    return sort_input_evenly(sublist_count, input_to_sort)


def sort_by_max_sublist_length(
    max_sublist_length, input_to_sort, even_sorting=True
):
    # make sure even_sorting is true/false
    assert check.input_is_true_or_false(even_sorting, "even_sorting")

    if even_sorting is True:
        return sort_evenly_given_max_sublist_length(
            max_sublist_length, input_to_sort
        )
    elif even_sorting is False:
        return sort_unevenly_given_max_sublist_length(
            max_sublist_length, input_to_sort
        )


def sort_evenly_given_max_sublist_length(max_sublist_length, input_to_sort):
    # sort input as evenly as possible given the max_sublist_length
    # NOTE: sublist(s) at maxumium length will only occcur if length of input_to_sort is evenly divisble by max_sublist_length

    assert check.integer_is_between_min_and_max(
        max_sublist_length, 1, len(input_to_sort)
    )

    # determine the number of sublists
    sublist_count = determine_sublist_count_from_max_sublist_length(
        max_sublist_length, input_to_sort
    )
    return sort_input_evenly(sublist_count, input_to_sort)


def sort_unevenly_given_max_sublist_length(max_sublist_length, input_to_sort):
    # sort input and make sure you utilize the full max_sublist_length

    assert check.integer_is_between_min_and_max(
        max_sublist_length, 1, len(input_to_sort)
    )

    # determine the number of sublists
    sublist_count = determine_sublist_count_from_max_sublist_length(
        max_sublist_length, input_to_sort
    )

    return sort_input_unevenly(
        sublist_count, input_to_sort, max_sublist_length
    )


def determine_sublist_count_from_max_sublist_length(
    max_sublist_length, input_to_sort
):
    # if input_length is evenly divisble by max_sublist_length, then all sublists will be at max_sublist_length
    # otherwise we know there will be one additional sublist
    if len(input_to_sort) % max_sublist_length == 0:
        sublist_count = len(input_to_sort) // max_sublist_length
    else:
        # use // to make sure you get an integer and not a float
        sublist_count = len(input_to_sort) // max_sublist_length + 1
    return sublist_count
