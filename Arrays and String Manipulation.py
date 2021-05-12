# Arrays

# Strengths
# Fast Lookups O(1)
# Fast Appends O(1)

# Weaknesses
# Fixed Size
# Costly Inserts and Deletes O(n) -
#       other elements have to move over or close gaps to insert an element


# Array Slicing
#       involves taking a subset from an array and allocating a new array with those elements

# Ex: New list of elements from start to end
myList[start:end]

# Ex: New list of elements from start onwards by omitting end
myList[start:]

# Something to Consider
# When slicing, you are allocating a new list and copying elements from the original list to the new list
# This takes O(n) time and O(n) space, where n is the number of elements in the resulting list
tail_of_list = myList[1:]
return myList[1:]

for item in myList[1:]:
    pass  # This takes O(n) time and space


# In-Place Algorithm
#       in place function modifies data structures or objects outside of its own stack frame
#       considered destructive because the original input is modified during the function call
#       in place means without creating a new copy of the input
#       typically, in-place functions only create additional vairables that are O(1) space

# Out of place function
#   Doesn't make any changes that are visible to other functions

# O(1) space cost, but the input has been modified which can affect code outside the function
def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element

    # NOTE: no need to return anything - we modified
    # int_list in place


def square_list_out_of_place(int_list):
    # We allocate a new list with the length of the input list
    squared_list = [None] * len(int_list)

    for index, element in enumerate(int_list):
        squared_list[index] = element ** 2

    return squared_list

# Only use an in-place algorithm if you're space constrained or positive you wont need the original input again


# Dynamic Array

# Strength: Automatic resizing (expands as your add more elements)
#   Fast Lookups: O(1)
#   Variable Size: add as many items as you want and it will expand
#   Cache-friendly: Dynamic arrays place items next to each other in memory

# Weaknesses
#   Slow worst-case appends: adding a new element @ the end of the dynamic array takes O(1) time
#           But if the dynamic array doesn't have room for the item, it will take O(n)
#   Costly Insert and Deletes: Elements are stored adjacent to each other
#           So adding and removing an item in the middle of the array requires scooting over other elements
#           This takes O(n) time
# In python, dynamic arrays are called lists
gas_prices = []
gas_prices.append(346)
gas_prices.append(360)
gas_prices.append(354)
