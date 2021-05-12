# Examples


# O(1) Time - Constant Time Relative to its Input
# Regardless of the input, it will require just one step tp print the first element of the list
def print_first_item(items):
    print(items[0])


# O(1) Time - Constant Time
def print_all_items(items):
    for item in items:
        print(item)


# O(n^2) Time or Quadratic Time
# Outer Loop runs N times and inner loop runs n times
def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)


# N could be the actual input, or the size of the input
# Both of these functions have O(n) runtime

def say_hi_n_times(n):
    for time in range(n):
        print("hi")


def print_all_items(items):
    for item in items:
        print(item)


# Drop the Constants
# This is O(2n) which is O(n)
def print_all_items_twice(items):
    for item in items:
        print(item)

    for item in items:
        print(item)

# This is O(1 + n/2 + 100), which we just call O(n)
# For big O Notation, were looking at what happens when n gets arbitrarily large


def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])

    middle_index = len(items) // 2
    index = 0
    while index < middle_index:
        print(items[index])
        index += 1

    for time in range(100):
        print("hi")


# Drop Less Significant Terms
# This is O(n + n^2) which is O(n^2)
def print_all_numbers_then_all_pair_sums(numbers):
    print("these are the numbers:")
    for number in numbers:
        print(number)

    print("and these are their sums:")
    for first_number in numbers:
        for second_number in numbers:
            print(first_number + second_number)


# Worst Case
# Sometimes worst case is significantly worse than best case
# this function is considered O(n) because that is worst case
# Best case scenario is O(1) where the needle is the first iteration
def contains(haystack, needle):

    # Does the haystack contain the needle?
    for item in haystack:
        if item == needle:
            return True

    return False


# Space Complexity

# O(1) space because there is a fixed number of variables
def say_hi_n_times(n):
    for time in range(n):
        print("hi")

# O(n) space - the size of hi_list scales with the size of the input
# Creating a new array that gets larger


def list_of_hi_n_times(n):
    hi_list = []
    for time in range(n):
        hi_list.append("hi")
    return hi_list


# Space complexity refers to additional space (not including the inputs)
# O(1) - constant space
def get_largest_item(items):
    largest = float('-inf')
    for item in items:
        if item > largest:
            largest = item
    return largest
