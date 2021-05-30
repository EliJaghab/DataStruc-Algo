def factorialIterative(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


print(factorialIterative(6))


def factorialRecursive(n):
    if n == 1:
        return n
    return n * factorialRecursive(n-1)


# Space O(n)
# Time O(n)


print(factorialIterative(6))
