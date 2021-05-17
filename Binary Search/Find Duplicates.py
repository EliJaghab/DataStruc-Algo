# O(n) Time
# O(n) Space

def findRepeat(nums):
    seen = set()
    for i in numbers:
        if i in seen:
            return i
        else:
            seen.add(i)


# O(1) Time
# O(n^2) Space

def findRepeat(nums):
    for index in range(1, len(nums)):
        seen = False
        for duplicate in nums:
            if index == duplicate:
                if seen:
                    return duplicate
                else:
                    seen = True


# time O(nlogn)
# Space O(1)

# 1. Do an in-place sort
# 2. Return when two adj numbers are the same

def find_repeat(numbers):
    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1]:
            return numbers[i]
