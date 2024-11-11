from typing import List


def maximize_profit_naive(prices: List[int]) -> int:
    max_profit = 0

    for left_ptr, buy_price in enumerate(prices):
        for sell_price in prices[left_ptr:]:
            profit = sell_price - buy_price

            message = f'Purchase Price: {buy_price}\nSell Price: {sell_price}\nProfit: {profit}'

            print(message)
            print()
            print()

            if profit > max_profit:
                max_profit = profit

    return max_profit


def maximize_profit(prices: List[int]) -> int:
    # Algorithm has minimum time complexity of O(n) since the stock price on each day must be checked
    max_profit = 0
    lowest_price = prices[0]

    # Check the price for each day
    for index, price in enumerate(prices[1:]):
        # If we can sell for a higher profit on this day, update the sale
        if price - lowest_price > max_profit:
            print(f'Potential profit: {price - lowest_price}')
            max_profit = price - lowest_price
        elif price < lowest_price:
            lowest_price = price
            print(f'New lowest price: {lowest_price}')

    return max_profit


print(f'Maximum Profit: {maximize_profit([7, 1, 5, 3, 6, 4])}')
print(f'Maximum Profit: {maximize_profit([7, 6, 4, 3, 1])}')
