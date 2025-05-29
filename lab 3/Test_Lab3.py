import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 95, 105, 110]
    test_arr = [11, 12, 22, 25, 34, 64, 90, 95, 105, 110]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 95, 105, 110]
    test_arr = [110, 105, 95, 90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_more_than_10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 88, 75, 43, 23]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)

def test_bubble_sort_less():
    result = []
    input_arr = [64, 34, 25, 12, 22]
    test_arr = [12, 22, 25, 34, 64]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == test_arr)

def test_bubble_check_int():
    result = []
    input_arr = [45, 10, 20, 15, "dog", 6, 7]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == 2)

def test_bubble_sort_empty():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == 0)