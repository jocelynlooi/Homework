def profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price-min_price > max_profit:
            max_profit = price - min_price

    return max_profit

prices_input= input()
prices = list(map(int,prices_input.split()))
result = profit(prices)
print(result)