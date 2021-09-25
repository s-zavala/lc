#!/usr/bin/env python3
import unittest

def generate(numRows: int) -> list[list[int]]:
    """
    Parameters: numRows number of rows
    
    Return: rows of numbers of Pascal's triangle

    """
    def row_n(n: int) -> list[int]:
        def backup_solution(n):
            from math import comb
            pascal = []
            for k in range(n+1):
                pascal.append(comb(n,k))
            return pascal
        # Start with an array of 1 and None.
        pascal = [1]
        for c in range(1, n+1):
            previous = pascal[-1]
            fraction = (n + 1 - c) / c
            pascal.append(int(previous * fraction))
        if pascal[-1] == 1:
            return pascal
        else:
            return backup_solution(n)
    
    pascals_triangle = []
    for n in range(numRows):
        if n == 0:
            pascals_triangle.append([1])
        else:
            pascals_triangle.append(row_n(n))
    return pascals_triangle

class TestGenerate(unittest.TestCase):

    def test_example_1(self):
        numRows = 5
        exp = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        act = generate(numRows)
        self.assertEqual(act, exp)
    
    def test_example_2(self):
        numRows = 1
        exp = [[1]]
        act = generate(numRows)
        self.assertEqual(act, exp)
    
    def test_fifteen(self):
        numRows = 15
        exp = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1],[1,10,45,120,210,252,210,120,45,10,1],[1,11,55,165,330,462,462,330,165,55,11,1],[1,12,66,220,495,792,924,792,495,220,66,12,1],[1,13,78,286,715,1287,1716,1716,1287,715,286,78,13,1],[1,14,91,364,1001,2002,3003,3432,3003,2002,1001,364,91,14,1]]
        act = generate(numRows)
        self.assertEqual(act, exp)

if __name__ == "__main__":
    unittest.main()
