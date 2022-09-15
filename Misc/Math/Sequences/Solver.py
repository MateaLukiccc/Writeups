from sympy import *
import time
##################################################################################################################################################################
st=time.time()
#1.find A

A=Matrix([[21, 301, -9549, 55692],
          [1,    0,     0,     0],
          [0,    1,     0,     0],
          [0,    0,     1,     0]]
         )
#print("A= \n",A)

#2.find eigenvectors and matrix S

S = Matrix([[1728, 2197, 4913, -9261],
            [144,   169,  289,   441],
            [12,     13,   17,   -21],
            [1,       1,    1,     1]]
           )
print('matrix S:\n', S.inv())


#step 3: find diagonal matrix
diagonal_matrix = S.inv()*A*S
#print('diagonal matrix:\n', diagonal_matrix)
'''
12 0 0 0
0 13 0 0
0 0 17 0
0 0 0 -21
'''
#B=S.inv()*Matrix([[4],[3],[2],[1]])

#print(B)

f1=lambda n: S*(diagonal_matrix**n)*S.inv()*Matrix([[4],[3],[2],[1]])         #exe time ~125s   =.sol = f(ITERS)[-1]


############################################### GIVEN CODE #################################################################

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfe7d7086e788af7922b")


import hashlib
import sys


# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

#######################################################################################################################################################

from gmpy2 import mpz
f=lambda n: (1612*(mpz(-21)**int(n)) + 981920*(mpz(12)**int(n)) - 1082829*(mpz(13)**int(n)) + 141933*(mpz(17)**int(n)))//42636 #exe time ~1.1s

if __name__ == "__main__":
    
    sol = f(ITERS)
    et=time.time()
    decrypt_flag(sol)
    print("and the exe time is ",et-st) # prints picoCTF{===REDACTED===}
    
   