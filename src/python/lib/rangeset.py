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

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Callable
Type = TypeVar('Type')

class SortedMultiset(Generic[Type]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[Type] = []) -> None:
        # Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)
        a = list(a)
        n = self.size = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

        # vvv RangeSet vvv
        c = [ai[1]-ai[0] for ai in a]
        self.c = [c[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]
        self.c_sum = [sum(c[n * i // num_bucket : n * (i + 1) // num_bucket]) for i in range(num_bucket)]
        # ^^^ RangeSet ^^^

    def __iter__(self) -> Iterator[Type]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[Type]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return 'SortedMultiset' + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return '{' + s[1 : len(s) - 1] + '}'

    def _position(self, x: Type) -> tuple[list[Type], int, int]:
        # return the bucket, index of the bucket and position in which x should be. self must not be empty.
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))
    
    def _position_less(self, x: Type) -> tuple[list[Type], int, int]:
        a, b, i = self._position(x)
        if i == 0:
            i = len(self.a[b-1])-1
            return self.a[b-1], b-1, i
        else:
            return a, b, i-1

    def __contains__(self, x: Type) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def count(self, x: Type) -> int:
        # Count the number of x.
        return self.index_right(x) - self.index(x)

    def add(self, x: Type) -> None:
        # Add an element. / O(√N)
        if self.size == 0:
            self.a = [[x]]
            cnt = x[1]-x[0]
            
            # vvv RangeSet vvv
            self.c = [[cnt]]
            self.c_sum = [cnt]
            self.size = 1
            # ^^^ RangeSet ^^^
            return
        a, b, i = self._position(x)
        a.insert(i, x)

        # vvv RangeSet vvv
        c = self.c[b]
        cnt = x[1]-x[0]
        c.insert(i, cnt)
        self.c_sum[b] += cnt
        # ^^^ RangeSet ^^^

        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]
            
            # vvv RangeSet vvv
            self.c[b:b+1] = [c[:mid], c[mid:]]
            self.c_sum[b:b+1] = [sum(c[:mid]), sum(c[mid:])]
            # ^^^ RangeSet ^^^
    
    def _pop(self, a: list[Type], b: int, i: int) -> Type:
        ans = a.pop(i)

        # vvv RangeSet vvv
        cnt = self.c[b][i]
        self.c[b].pop(i)
        self.c_sum[b] -= cnt
        # ^^^ RangeSet ^^^

        self.size -= 1
        if not a:
            del self.a[b]

            # vvv RangeSet vvv
            del self.c[b]
            del self.c_sum[b]
            # ^^^ RangeSet ^^^
        return ans
    
    # vvv RangeSet vvv
    def rangecnt(self, left: int, right: int) -> int:
        INF = self[0][0]
        ret = 0
        a, b_left, i_left = self._position_less((left, INF))
        l, r = a[i_left]
        ret += max(0, min(r, right)-max(l, left))
        a, b_right, i_right = self._position_less((right, INF))
        if b_left == b_right and i_left == i_right: return ret
        l, r = a[i_right]
        ret += max(0, min(r, right)-max(l, left))
        if b_left == b_right:
            ret += sum(self.c[b_left][i_left+1:i_right])
        else:
            ret += sum(self.c[b_left][i_left+1:])
            ret += sum(self.c[b_right][:i_right])
            ret += sum(self.c_sum[b_left+1:b_right])
        return ret
    # ^^^ RangeSet ^^^

    def discard(self, x: Type) -> bool:
        # Remove an element and return True if removed. / O(√N)
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True

    def lt(self, x: Type) -> Type | None:
        # Find the largest element < x, or None if it doesn't exist.
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: Type) -> Type | None:
        # Find the largest element <= x, or None if it doesn't exist.
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: Type) -> Type | None:
        # Find the smallest element > x, or None if it doesn't exist.
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: Type) -> Type | None:
        # Find the smallest element >= x, or None if it doesn't exist.
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> Type:
        # Return the i-th element.
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> Type:
        # Pop and return the i-th element.
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: Type) -> int:
        # Count the number of elements < x.
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: Type) -> int:
        # Count the number of elements <= x.
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans
    
# 参考: https://kkt89.hatenablog.com/entry/2020/10/14/std%3A%3Aset%E3%81%A7%E5%8C%BA%E9%96%93%E3%82%92%E7%AE%A1%E7%90%86%E3%81%99%E3%82%8B%E5%A5%B4

VType = TypeVar('VType')
class Node(Generic[VType]):
    def __init__(self, left: int, right: int, value: VType) -> None:
        self._left = left
        self._right = right
        self._value = value

    def __lt__(self, other: "Node") -> bool:
        return self.get_range() < other.get_range()
    
    def __le__(self, other: "Node") -> bool:
        return self.get_range() <= other.get_range()

    def __gt__(self, other: "Node") -> bool:
        return self.get_range() > other.get_range()
    
    def __ge__(self, other: "Node") -> bool:
        return self.get_range() >= other.get_range()
    
    def __eq__(self, other: "Node") -> bool:
        return self.get_range() == other.get_range()
    
    def __getitem__(self, i: int) -> int:
        if i == 0:
            return self._left
        elif i == 1:
            return self._right
        raise IndexError
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"({self._left}, {self._right}, {self._value})"

    def get_range(self):
        return (self._left, self._right)
    
    def left(self) -> int:
        return self._left
    
    def right(self) -> int:
        return self._right
    
    def value(self) -> VType:
        return self._value

class RangeSet(Generic[VType]):
    SENTINEL = 1<<60
    LEFT = -SENTINEL+1
    RIGHT = SENTINEL-1
    def __init__(self, add: Callable[[int, int, VType], None], delete: Callable[[int, int, VType], None], left: int = LEFT, right: int = RIGHT) -> None:
        self._left = left
        self._right = right
        self._add = add
        self._delete = delete
        self.data = SortedMultiset()
        self.data.add(Node(-RangeSet.SENTINEL, -RangeSet.SENTINEL, 0))
        self.data.add(Node(RangeSet.SENTINEL, RangeSet.SENTINEL, 0))
        self._cover_cnt = 0

    def add(self, left: int, right: int, value: VType):
        self.data.add(Node(left, right, value))
        self._add(left, right, value)

    def discard(self, left: int, right: int, value: VType):
        self.data.discard(Node(left, right, value))
        self._delete(left, right, value)

    def _le(self, node: Node) -> tuple[int, int, VType]:
        ret = self.data.le(node)
        return ret.left(), ret.right(), ret.value()
    
    def ge(self, node: Node) -> tuple[int, int, VType]:
        ret = self.data.ge(node)
        return ret.left(), ret.right(), ret.value()

    def insert(self, left: int, right: int, value: VType) -> None: # [left, right)
        assert self._left <= left
        assert right <= self._right
        assert left <= right
        if left == right: return
        
        l, r, v = self.le(Node(left, right, 0))
        if l <= left <= r:
            left = min(left, l)
            right = max(right, r)
            self.discard(l, r, v)
            self._cover_cnt -= r-l
        l, r, v = self.ge(Node(left, right, 0))
        while True:
            if left <= l <= right:
                right = max(right, r)
                self.discard(l, r, v)
                self._cover_cnt -= r-l
                l, r, v = self.ge(Node(left, right, 0))
            else: break
        self.add(left, right, value)
        self._cover_cnt += right-left

    def remove(self, left: int, right: int) -> None:
        assert self._left <= left
        assert right <= self._right
        assert left <= right
        if left == right: return
        
        l, r, v = self.le(Node(left, right, 0))
        if l <= left < r:
            self.discard(l, r, v)
            self._cover_cnt -= r-l
            if l < left:
                self.add(l, left, v)
                self._cover_cnt += left-l
            if right < r:
                self.add(right, r, v)
                self._cover_cnt += r-right
        l, r, v = self.ge(Node(left, right, 0))
        while True:
            if left <= l < right:
                self.discard(l, r, v)
                self._cover_cnt -= r-l
                if right < r:
                    self.add(right, r, v)
                    self._cover_cnt += r-right
                l, r, v = self.ge(Node(left, right, 0))
            else: break

    def mex(self) -> int:
        node = self.data[1]
        left, right = node.left(), node.right()
        if left > 0:
            return 0
        else:
            return right
    
    def __str__(self) -> str:
        return self.data.__str__()
    
    def cover_cnt(self, left: int = None, right: int = None) -> int:
        if left == None: left = self._left
        if right == None: right = self._right
        assert self._left <= left
        assert right <= self._right
        assert left <= right
        if self._left == left and self._right == right: return self._cover_cnt
        if left == right: return 0
        
        ret = self.data.rangecnt(left, right)
        return ret
    
    def uncover_cnt(self, left: int = None, right: int = None) -> int:
        if left == None: left = self._left
        if right == None: right = self._right
        assert self._left <= left
        assert right <= self._right
        assert left <= right

        return right-left - self.cover_cnt(left, right)
  
def call(l, r, v): pass
R = RangeSet(call, call, 0, (10**9)+1)
N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)

for a in C: R.insert(a, a+1, 0)

for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1
    C[A[i]] -= 1
    if C[A[i]] == 0:
        R.remove(A[i], A[i]+1)
    A[i] = x
    C[A[i]] += 1
    if C[A[i]] == 1:
        R.insert(x, x+1, 0)
    print(R.mex())
