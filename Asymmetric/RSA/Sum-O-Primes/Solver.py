from Crypto.Util.number import long_to_bytes
from sympy import * 
import math
import math
import sys

if sys.version_info < (3, 9):
    import gmpy2
    math.gcd = gmpy2.gcd
    math.lcm = gmpy2.lcm



x ="154ee809a4dc337290e6a4996e0717dd938160d6abfb651736d9f5d524812a659b310ad1f221196ee8ab187fa746a1b488a4079cddfc5db08e78be0d96c83c01e9bb42420b40d6f0ad9f220633459a6dc058bb01c517386bfbd2d4811c9b08558b0e05534768581a74884758d15e15b4ef0dbd6a338bf1f52eed4f137957737d2"
n = "6ce91e471f1df651b0d275d6d5522703feecdd77e7821a2caf9514104c059781c1b2e64772d9220addd657ecbd4e6cb8b5941608f6ab54bd5760074a5cd5854920439422192d2ee8912f1ebcc0d97714f209ee2a22e2da60e071541cb7e0772373cfea71831673378ee6432e63abfd14db0d4aa601928923253f9edd419ce96f4d68ce0aa3e6d6b530cd46eefbdac93038ce949c9dd2e573a47471cf8223f88b96e00a92f4d47fd277c42c4075b5e99b41a9f279f442bc0d533b9ddc50592e369e7026b3f7afaa8edf8972f0c3055f4de67a0eea963f099a32e1539de1d1727abadd9235f66371998ec883d1f89b8d907270842818cae49cd5c7f906c4752e81"
c ="48b89662b9718fb391c96527272bf74c27810edaca09b63e694af9d11608010b1db9aedd1c867849371121941a1ccac610f7b28b92fa2f981babe816e6d3ecfab83514ed7e18e2b23fc3b96c7002ff47da897e9f2a9cb1b4e245396589e0b72affb73568a2016031555d2a46557919e44a15cd43fe9e1881d40dce1d1e36625e63b1472d3c317898102943072e06d79688c96b6ee2e584002c66497a9cdc48c38aa0548a7bc4fed9b4c23fcd493f38ece68788ef37a559b7f20c6941fcf8e567d9f50807259a7f11fa7a01d3125a1f7609cd94781f224ec8351605354b11c6b078fe015826342c3271ee3af4b99bb0a538b1e6b845594ee6546be8abd22ef2bd"



sum = int(x,16)
n = int(n, 16)
e = 65537
ct = int(c,16)

# x=p+q     n=p*q
# p=x-q     n=(x-q)*q=xq-q^2=>  q^2-xq+n=0





a = 1
b = sum
c = n

x = Symbol('x')

#q=solve(q^2-xq+n)

p = (int(max(solve(a*x**2 - b*x + c, x)))) 
q = (int(min(solve(a*x**2 - b*x + c, x)))) 
#print(p)
#print(q)

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)
pt = pow(ct, d, n)
print(long_to_bytes(pt))