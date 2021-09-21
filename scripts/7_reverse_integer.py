#!/usr/bin/env python3

def reverse(x:int) -> int:
    if x == 0: return x
    if x < 0:
        x *= -1
        flag = False
    else:
        flag = True
    arr = [None]*10
    for i in range(10):
        if len(str(x)) == 1 and x == 0:
            arr[i] = None
        else:            
            arr[i] = x % 10
            x = x // 10
    s = ''
    if not flag:
        bound = 2147483648
    else:
        bound = 2147483647
    for i in range(10):
        if arr[i] == None: continue
        s += str(arr[i])
    ans = int(s)
    if ans > bound: return 0
    if not flag:
        return ans * -1
    else:
        return ans

def reverse2(x: int) -> int:
    if not x: return 0
    if x < 0:
        x *= -1
        flag = False
    else:
        flag = True
    s = str(x)
    l = list(s)
    l.reverse()
    ans = ''
    for i in l:
        ans += i
    int_ans = int(ans)
    if x > 0:
        bound = 2147483647
    else:
        bound = 2147483648
    if int_ans > bound: return 0
    elif not flag:
        return (int_ans * -1)
    else:
        return int_ans 

def reverse3(self, x):
        sign = (x > 0) - (x < 0)
        rev = int(str(x*sign)[::-1])
        return sign*rev * (rev < 2**31)

if __name__ == "__main__":
    tests = {
        100001: 100001,
        2147483648: 0,
        -2147483648: 0,
        -123: -321
    }
    for x in tests.keys():
        print(f"x - {x}")
        print(f"Expected answer - {tests[x]}")
        print(f"Actual answer- {reverse2(x)}")