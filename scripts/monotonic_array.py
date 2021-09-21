# class Solution:
def isMonotonic(A: list[int]) -> bool:
    # def ver1(A):
    #     incr = False
    #     decr = False
    #     if A[0] > A[1]: incr = True
    #     elif A[0] < A[1]: decr = True
    #     elif A[0] == A[1]: A.pop(0)
    # def ver2(A):
    #     B = A[:]
    #     B.sort()
    #     C = A[:]
    #     C.sort(reverse=False)
    #     if A == B: return True
    #     if A == C: return True
    #     return False
    # def solution(A):
    incr = all(A[i] <= A[i+1] for i in range(len(A) - 1))
    decr = all(A[i] >= A[i+1] for i in range(len(A) - 1))
    return incr or decr

if __name__ == "__main__":
    print(isMonotonic(A=[6,5,4,4]))