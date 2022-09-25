import random
import time
import gmpy2
from pwn import *
from Crypto.Util.number import *
from itertools import combinations

#have to guess e and then common modulus


p = remote("be.ax" ,31124)
# Record start time
start_time = int(time.time()) 

# Get modulus
p.recvuntil("is: ")
n = int(p.recvuntil('\n')[:-1])
p.sendlineafter(": ","1")

# Get two different ciphertext of flag
p.recvuntil("encrypted flag: ")
c1 = int(p.recvuntil('\n')[:-1],16)
p.sendlineafter(": ","1")

p.recvuntil("encrypted flag: ")
c2 = int(p.recvuntil('\n')[:-1],16)

# Code get from https://infosecwriteups.com/rsa-attacks-common-modulus-7bdb34f331a5
def attack(c1, c2, e1, e2, N):
    s1 = inverse(e1,e2)
    s2 = int((gmpy2.gcd(e1,e2) - e1 * s1) // e2)
    temp = inverse(c2, N)
    m1 = pow(c1,s1,N)
    m2 = pow(temp,-s2,N)
    return long_to_bytes((m1 * m2) % N)

# Server time will delay abit so brute force the time
for i in range(5):
    random.seed(start_time-i)
    possible_e = []
    # Generate 10 possible e
    for _ in range(10):
        possible_e.append(random.randint(1, n))

    # Generate the combination of 2 possible e
    comb = combinations(possible_e, 2)
    for e1,e2 in list(comb):
        if gmpy2.gcd(e1,e2):
            m = attack(c1, c2, e1, e2, n)
            # If flag format in message found the flag!
            if b"corctf" in m:
                print(m)
# b'corctf{y34h_th4t_w4snt_v3ry_h1dd3n_tbh_l0l}\n'