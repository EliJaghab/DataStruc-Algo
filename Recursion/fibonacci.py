def fibIterative(n):
    if n < 2:
        return n
    a = 0
    b = 1
    total = 0
    for i in range(n-1):
        total = a + b
        a = b
        b = total
    return total


def fibRecursive(n):
    if n < 2:
        return n
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)
