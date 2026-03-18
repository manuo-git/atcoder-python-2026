# https://atcoder.jp/contests/language-test-202505/submissions/70682654
#Reference: https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
class DSU:
    '''
    Disjoint Set Union for codon, PyPy3
    '''
    N: int
    _parent: list[int]
    __slots__ = ('N', '_parent')
    def __init__(self, N: int) -> None:
        self.N = N
        self._parent = [-1] * N
    def leader(self, Vi: int) -> int:
        assert 0 <= Vi < self.N
        Pi = Vi
        while self._parent[Pi] >= 0:
            Pi = self._parent[Pi]
        while Pi != Vi:
            self._parent[Vi], Vi = Pi, self._parent[Vi]
        return Pi
    def merge(self, Ui: int, Vi: int) -> int:
        assert 0 <= Ui < self.N and 0 <= Vi < self.N
        Pi, Ci = self.leader(Ui), self.leader(Vi)
        if Pi != Ci:
            if self._parent[Pi] > self._parent[Ci]:
                Pi, Ci = Ci, Pi
            self._parent[Pi] += self._parent[Ci]
            self._parent[Ci] = Pi
        return Pi
    def same(self, Ui: int, Vi: int) -> bool:
        assert 0 <= Ui < self.N and 0 <= Vi < self.N
        return self.leader(Ui) == self.leader(Vi)
    def size(self, Vi: int) -> int:
        assert 0 <= Vi < self.N
        return - self._parent[ self.leader(Vi) ]
    def groups(self) -> list[list[int]]:
        buffer: list[int] = [-1] * self.N
        G: list[list[int]] = []
        for now in range(self.N):
            Pi = now
            while self._parent[Pi] >= 0:
                Pi = self._parent[Pi]
            Bi = buffer[Pi]
            if Bi == -1:
                Bi = buffer[Pi] = len(G)
                G.append([-1] * (- self._parent[Pi]))
            G[Bi][-1] += 1
            G[Bi][G[Bi][-1]] = now
            while Pi != now:
                self._parent[now], now = Pi, self._parent[now]
        return G