from random import *

# randint(L, R) -> [L, R]の範囲でランダム
N = 4
A = [randint(1, 10) for _ in range(N)]
print(N)
print(*A)