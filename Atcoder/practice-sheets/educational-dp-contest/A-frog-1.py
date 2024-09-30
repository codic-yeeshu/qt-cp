'''
Problem Statement : https://atcoder.jp/contests/dp/tasks/dp_a
'''

import sys
sys.setrecursionlimit(10**6)

def minPrice(start, end, prices, memo):
    if start == end:
        return 0
    if (start, end) in memo:
        return memo[(start, end)]

    next_cost = abs(prices[start] - prices[start+1]) + minPrice(start+1, end, prices, memo)
    skip_cost = float('inf')
    if start + 2 <= end:
        skip_cost = abs(prices[start] - prices[start+2]) + minPrice(start+2, end, prices, memo)
    
   
    memo[(start, end)] = min(next_cost, skip_cost)
    return memo[(start, end)]

n = int(input())
prices = list(map(int, input().split()))
print(minPrice(0, n-1, prices, {}))