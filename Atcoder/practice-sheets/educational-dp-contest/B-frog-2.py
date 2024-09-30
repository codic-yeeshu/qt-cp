'''
    Problem Statement: https://atcoder.jp/contests/dp/tasks/dp_b
'''
import sys
sys.setrecursionlimit(10**6)

def minPrice(start, end, k, prices, memo):
    if start == end:
        return 0
    if start in memo:
        return memo[start]
    
    res = float('inf')
    for i in range(1, k+1):
        
        if start + i <= end:
            kstep = abs(prices[start] - prices[start+i]) + minPrice(start+i, end, k, prices, memo)
        
            
        res = min(res, kstep)
    memo[start] = res
    return memo[start]
        

n, k = map(int, input().split())
prices = list(map(int, input().split()))

print(minPrice(0, n-1, k, prices, {}))