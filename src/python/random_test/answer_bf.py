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

N = int(input())
A = list(map(int, input().split()))

def calc(a):
    while a&1 == 0:
        a //= 2
    return a

ans = 0
for i in range(N):
    res = 0
    for j in range(i+1):
        res += calc(A[i]+A[j])
    # print(res)
    ans += res
print(ans)