#!/usr/bin/env python3
import unittest


def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    m = len(mat)
    n = len(mat[0])
    mxn = [None]*(m*n)
    rxc = []
    for i in range(m):
        for j in range(n):
            mxn[(i*n+j)] = mat[i][j]
    elem_per_row = m*n//r
    for i in range(r):
        rxc.append([None]*c)
        for j in range(elem_per_row):
            rxc[i][j] = mxn[(i*elem_per_row+j)]
    return rxc

def matrixReshape2(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    newList = [[]]
    if r*c != len(mat)*len(mat[0]):
        return mat
    else:
        for row in mat:
            for item in row:
                if len(newList[-1])<c:
                    newList[-1].append(item)
                else:
                    newList.append([])
                    newList[-1].append(item)
    return(newList)

class TestMatrixReshape(unittest.TestCase):

    def test_eg1(self):
        mat = [[1,2],[3,4]]; r = 1; c = 4
        exp = [[1,2,3,4]]
        act = matrixReshape2(mat, r, c)
        self.assertEqual(act, exp)
    
    def test_eg2(self):
        mat = [[1,2],[3,4]]; r = 2; c = 4
        exp = [[1,2],[3,4]]
        act = matrixReshape2(mat, r, c)
        self.assertEqual(act, exp)

if __name__ == "__main__":
    unittest.main()