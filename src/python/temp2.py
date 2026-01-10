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
MOD = 998244353 #10**9+7
INF = 1<<60
Yes, No = "Yes", "No"

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
memo = [[0]*W for _ in range(H)]
flipvote = [[0, 0] for _ in range(H)]

for i in range(H):
    if sum(flipvote[i]) == 2:
        print(-1)
        exit()
    for j in range(W-1):
        if A[i][j] == A[i][j+1]:
            memo[i][j] = 1
            memo[i][j+1] = 1
    for j in range(W):
        if memo[i][j] == 0:
            if i < H-1:
                print(-1)
                exit()
            else:
                if A[i][j] == A[i+1][j]:
                    flipvote[i+1][0] = 1
                else:
                    flipvote[i+1][1] = 1
                
    print(i, memo[i])
print(flipvote)