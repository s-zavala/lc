#!/usr/bin/env python3
import unittest


def maxProfit(prices: list[int]) -> int:
    if sorted(prices, reverse=True) == prices:
        return 0
    buy = float("inf")
    profit = float("-inf")
    for num in prices:
        if num < buy:
            buy = num
        else:
            diff = num - buy
            if diff > profit:
                profit = diff
    return profit

class TestBestBuySell(unittest.TestCase):
    
    def test_eg1(self):
        prices = [7,6,4,3,1]
        exp = 0
        act = maxProfit(prices)
        self.assertEqual(act, exp)
    
    def test_eg2(self):
        prices = [7,1,5,3,6,4]
        exp = 5
        act = maxProfit(prices)
        self.assertEqual(act, exp)

if __name__ == "__main__":
    unittest.main()