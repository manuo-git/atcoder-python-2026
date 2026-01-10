from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from atcoder.fenwicktree import FenwickTree
from atcoder.segtree import SegTree
from atcoder.lazysegtree import LazySegTree
from atcoder.string import suffix_array, z_algorithm, lcp_array
from atcoder.dsu import DSU
from itertools import permutations, combinations, groupby
from functools import cache
from heapq import heappop, heappush
import math, sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
_int = lambda x: int(x)-1
MOD = 10**9+7
INF = 1<<60
Yes, No = "Yes", "No"

N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def calc(m):
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                dp[i][j] = m
            else:
                dp[i][j] = A[i][j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    res = 0
    for i in range(N):
        for j in range(i+1, N):
           if dp[i][j] <= P: res += 1
    return res

def check(m):
    res = calc(m)
    return res >= K

def check1(m):
    res = calc(m)
    return res <= K

res = calc(INF)
if res == K:
    print("Infinity")
elif res > K:
    print(0)
else:
    l, r = 1, 10**10
    while r-l>1:
        m = (l+r)//2
        if check(m): l = m
        else: r = m
    if calc(l) != K:
        print(0)
    else:
        right = l
        l, r = 1, l
        while r-l>1:
            m = (l+r)//2
            if check1(m): r = m
            else: l = m
        print(right-r+1)