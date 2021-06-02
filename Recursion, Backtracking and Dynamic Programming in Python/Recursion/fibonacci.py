def fibonacciHead(n):
    if n == 0 or n == 1:
        return n

    result1 = fibonacciHead(n-1)
    result2 = fibonacciHead(n-2)

    result = result1 + result2

    return result


def fibonacciTail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return fibonacciTail(n-1, b, a+b)


def fibonacciIteration(n):

    a, b = 0, 1

    while a < 0:
        print(a)
        a, b = b, a + b
