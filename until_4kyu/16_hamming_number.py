from collections import defaultdict


def hamming(n):
    ham = defaultdict(lambda: 1, {1: 1})
    exp = [0, 0, 0]
    base = [2, 3, 5]
    mult = base.copy()
    for i in range(1, n):
        ham[i] = min(mult)
        if mult[0] == ham[i]:
            exp[0] += 1
            mult[0] = base[0] * ham[exp[0]]
        if mult[1] == ham[i]:
            exp[1] += 1
            mult[1] = base[1] * ham[exp[1]]
        if mult[2] == ham[i]:
            exp[2] += 1
            mult[2] = base[2] * ham[exp[2]]
    return ham[n - 1]


assert hamming(1) == 1
assert hamming(2) == 2
assert hamming(3) == 3
assert hamming(4) == 4
assert hamming(5) == 5
assert hamming(6) == 6
assert hamming(7) == 8
assert hamming(8) == 9
assert hamming(9) == 10
assert hamming(10) == 12
assert hamming(11) == 15
assert hamming(12) == 16
assert hamming(13) == 18
assert hamming(14) == 20
assert hamming(15) == 24
assert hamming(16) == 25
assert hamming(17) == 27
assert hamming(18) == 30
assert hamming(19) == 32
