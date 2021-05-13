def canPermutePalindrome(self, s: str) -> bool:

    unpaired = set()

    for i in s:
        if i in unpaired:
            unpaired.remove(i)
        else:
            unpaired.add(i)

    if len(unpaired) <= 1:
        return True
    return False

# O(n) Time
# O(n) Space
