def reverse(list_of_chars):

    start, end = 0, len(list_of_chars) - 1

    while start <= end:
        list_of_chars[start], list_of_chars[end] = list_of_chars[end], list_of_chars[start]
        start += 1
        end -= 1


# O(n) time
# O(1) space
