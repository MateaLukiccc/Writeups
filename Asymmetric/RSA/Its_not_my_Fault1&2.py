import sys
!{sys.executable} -m pip install tqdm


from pwn import remote, process
from hashlib import md5
from sage.all import *
from itertools import product
import string
from random import randint
from sage.all import *
from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pContext, ntl_ZZ_pX

def poly_fast_ntl(ctx, f, xs):
    n = len(xs)
    k = ceil(log(n, 2))
    if (2 ** k) > n:
        xs = xs + [0] * ((2 ** k) - n)

    def build_tree(xs, k):
        M = {}
        for j in range(0, 2 ** k):
            M[(0, j)] = ntl_ZZ_pX([-xs[j], 1], ctx)
        for i in range(1, k + 1):
            for j in range(0, 2 ** (k - i)):
                M[(i, j)] = M[(i - 1, 2 * j)] * M[(i - 1, 2 * j + 1)]
        return M

    def compute(f, xs, k, M, s=0):
        if k == 0:
            yield f
            return
        r0 = f % M[(k - 1, 2 * s)]
        r1 = f % M[(k - 1, 2 * s + 1)]
        mid = len(xs) // 2
        yield from compute(r0, xs[:mid], k - 1, M, 2 * s)
        yield from compute(r1, xs[mid:], k - 1, M, 2 * s + 1)

    M = build_tree(xs, k)
    ans = list(compute(f, xs, k, M))
    # Using int instead of Integer will overflow...
    return [Integer(pl.list()[0]) for pl in ans[:n]]

'''
conn = remote("mercury.picoctf.net", 53988)


def solve_pow():
    line = conn.recvline().decode().strip()
    prefix = line[33:38]
    suffix = line[-6:]
    print(f"md5({prefix} + ???) = ??? + {suffix}")
    for x in product(string.printable, repeat=10):
        s = prefix + "".join(x)
        if md5(s.encode()).hexdigest()[-6:] == suffix:
            conn.sendline(s)
            break


solve_pow()
'''
#adjust for future use
n = 124820867833961512255121751609049306179897666404096891662718071264088624606195417583639161066276975279640599118437354335640828498035985542095139168119692839404116968042389114810846687132156292424607681366934277727898599922856113752913454673986423798381847193428071452354375463030105066256138253881897882994099
e = 46413346084333645012143147319389347924397373027897998120051654242937480130282545034433967290231436105403203157816717530203079607233722565425714290923944628662988841561125900662835135189696637301075373141006198752365262569240099036001408525284187514463343741272674488593785654318061637768053550355072803501569
print(n)
print(e)

#we need to adjust bits which is upper bound fro d_p
BITS = 36

from tqdm import tqdm


def square_root_attack():
    K = 1 << BITS
    D = 1 << (BITS // 2)
    Z = Zmod(n)
    x = Z(randint(2, n - 1))
    ctx = ntl_ZZ_pContext(n)
    xe = x ** e
    f_fac = []
    for i in tqdm(range(0, D)):
        f_fac.append(ntl_ZZ_pX([-x, xe ** i], ctx))
    # NTL's polynomial multiplication is much faster
    f = sage.all.product(f_fac)  # Because itertools.product != sage.all.product
    xed = xe ** D
    ys = [xed ** b for b in range(0, D)]
    for t in poly_fast_ntl(ctx, f, ys):
        p = gcd(t, n)
        if p > 1 and p < n:
            assert n % p == 0
            q = n // p
            return p, q


# if e*d_p != 1 (mod p), it will be infinite loop
while (r := square_root_attack()) is None:
    pass

p, q = r
ans = str(p + q)
print(p,q,ans)
