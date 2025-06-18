import math 
"""
results in TLEs, need to add memoization
* map {factor: [nums with it as a factor]}
- for num1=3 in list: get all factors: 
    -  set L,R = 1, num1=3
        - if L*R = num1, add them EACH as a key to factormap: {1: [3], 3:[3]}
        - then do L++, R-- -> 
    -> factors = 1, 3, 
* {3: [3]}
- for num2=14 
    - check if in list (if yes, done, just update map) -> no
    - check factors: 
        - L,R = 1,14 -> check both divide cleanly into num2 -> map both -> increment/decrement
        - L,R = 2, 13 -> check both divide cleanly -> map 2 and num2/2 -> update L,R = 3,(otherfactor=7)-1
        - L,R = 3, 6 -> check both -> map neither -> increment/decrement
        - L,R = 4,5 -> check both -> map neither -> increment/decrement -> L >=R SO STOP (end condition)
        * diff to map: {1:[14], 2:[14], 7:[14]}
        * final map: {1:[3, 14], 2:[14], 3:[3], 7:[14]}}
- for num3=15
    - check if in list (if yes, done, just update map) -> no
    - check factors:
        - L,R = 1,15 -> check both divide cleanly into num3 -> map both -> incr/decr
        - L,R = 2,14 NOTE: num3 is ODD, so skip evens
        - L,R = 3, 13 -> check both -> map 3 and num3/3=5 -> update L,R=4, (otherfactor=5)-1 aka 4, 
"""
# https://cses.fi/problemset/task/1081/

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
nums = list(map(int, data[1:]))

# n, nums = 5, [3,14,15,7,9] # output = 7


"""
def commonDivisors(nums):
    factorMap = {}
    for num in nums:
        left, right = 1, num
        while left < right: 
            if (num/left).is_integer():
    
                factorMap.setdefault(int(left), []).append(num)
                factorMap.setdefault(int(num/left), []).append(num)
                
                right = int(num/left) - 1
                left += 1
                
            elif (num/right).is_integer(): 
                print(num,right)
                factorMap.setdefault(int(right), []).append(num)
                factorMap.setdefault(int(num/right), []).append(num)

                right -=1
                left = int(num/right) + 1
            else:
                left += 1
                right -=1

        if left == right: 
            if (num/left).is_integer():
            
                factorMap.setdefault(left, []).append(num)

    
    maxKeyWith2 = float('-inf')
    for key, val in factorMap.items():
        if len(val) >= 2: maxKeyWith2 = max(maxKeyWith2, key)
    
    print(maxKeyWith2)
    return maxKeyWith2
"""

def commonDivisors(nums):
    factorMap = {}

    for num in nums: 
        cur_factors = []
        for i in range(1, math.ceil(math.sqrt(num)) + 1):
            if num % i == 0 and i not in cur_factors: 
                factorMap.setdefault(i, []).append(num)
                cur_factors.append(i)
                if i != int(num/i):
                    factorMap.setdefault(int(num/i), []).append(num)
                    cur_factors.append(int(num/i))
        
    maxKeyWith2 = float('-inf')
    for key, val in factorMap.items():
        if len(val) >= 2: maxKeyWith2 = max(maxKeyWith2, key)
    
    print(maxKeyWith2)
    return

commonDivisors(nums)