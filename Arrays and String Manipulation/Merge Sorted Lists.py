# O(nlogn) Approach

def merge_sorted_lists(arr1, arr2):
    return sorted(arr1 + arr2)


# O(n) and O(n) additional space
def merge_lists(my_list, alices_list):

    resultSize = len(my_list) + len(alices_list)
    result = [None] * resultSize

    aliceInd = myInd = indMerged = 0

    while indMerged < resultSize:
        myExhaust = myInd >= len(my_list)
        aliceExhaust = aliceInd >= len(alices_list)

        if (not myExhaust and (aliceExhaust or my_list[myInd] < alices_list[aliceInd])):
            result[indMerged] = my_list[myInd]
            myInd += 1
        else:
            result[indMerged] = alices_list[aliceInd]
            aliceInd += 1

        indMerged += 1
    return result


# LeetCode Solution with Larger Space for allocation
# https://leetcode.com/problems/merge-sorted-array/


# Time complexity O(n + m)
# Space Complexity O(1) -  in place
def merge(nums1, nums2, m, n):

    p1 = m - 1
    p2 = n - 1

    for p in range(m + n - 1, -1, -1):
        # P2 List is completed - Done
        if p2 < 0:
            break

        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1


# Merge Two Sorted Linked Lists
# https://leetcode.com/problems/merge-two-sorted-lists/


def mergeTwoLists(l1, l2):
    dummy = output = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            output.next = l1
            l1 = l1.next
        else:
            output.next = l2
            l2 = l2.next
    output = output.next

    # Add Remainder of Whichever List Still exists
    if l1:
        output.next = l1
    if l2:
        output.next = l2

    return dummy.next
