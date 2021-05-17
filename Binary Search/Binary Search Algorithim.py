#Binary Search finds an item in a sorted list in O(nlogn) time


def binary_search(target, nums):
    left, right = 0 , len(nums) - 1

    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1