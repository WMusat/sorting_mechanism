# sorting_mechanism
Take in a list and return a list of sublists 

This code's main function is to take an input list and then return a list of sublists.
There are 3 main paths:

1. `sort_evenly_given_sublist_count`

Input a list and the amount of sublists you would like.

The return will be a list of the requested amount of sublists - the contents of the initial input will be 'sorted' as evenly as possible amongst the sublists

```
Example:
    sublist_count = 5
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1, 6, 11], [2, 7], [3, 8], [4, 9], [5, 10]]
```

2. `sort_by_max_sublist_length and even_sorting = True`

Input a list and the maximum length of sublists you would like

The return will be a list of sublists, and the maximum length of the sublists will not exceed the requested size.

Note that the only way the maximum sublist size will be achieved in this scenario is if the length of the input and the max sublist length is evenly divisible

```
Example:
    max_per_sublist = 8
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10]]
```


3. `sort_by_max_sublist_length and even_sorting = False`

In put a list and the maximum lenght of sublists you would like

The return will be a list of sublists, and the maximum length of the sublists WILL be achieved as many times as possible.

This means the "sorting" of the inputs will not be even - so you could have 1 sublist of 10 items and 1 sublist of 1 item.
```
Example:
    max_per_sublist = 8
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11]]
```

Note that the "sorting" in this code refers to how the input is sorted amongst the sublists
the order in which the items appear in the initial input list will not necessarily be preserved
