def maxProfit(prices):
    maxProf = 0
    minPrice = prices[0]

    for price in prices:
        minPrice = min(prices, minPrice)
        maxProf = max(maxProf, price - minPrice)

    return maxProf


# O(1) space
# O(n) time
