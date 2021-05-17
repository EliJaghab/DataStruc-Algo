def findMin(nums):
    left, right = 0, len(nums) - 1

    # While the array is not sorted
    while nums[left] > nums[right]:

        mid = left + (right - left) // 2

        # If the right half of the array is sorted, check the left
        # Move the right point to the middle
        if nums[mid] < nums[right]:
            right = mid

        # If the right half of the array is not sorted
        # Move the left point to the middle + 1
        else:
            left = mid + 1

    return nums[left]

#Time: O(nlogn)
#Space: O(1)
