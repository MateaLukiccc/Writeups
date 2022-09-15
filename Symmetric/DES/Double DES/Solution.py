#its double encrypted with DES ECB mode 

import itertools
import string
from Crypto.Cipher import DES
from pwn import *

flag="d8e52aecf0112962949f4b62dc4b880c23105f24f3f87c107bd8884c784f683f0fac8cab25b14c79"



KEY_LEN=6
def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def all_possible_keys():
    return itertools.product(string.digits, repeat=KEY_LEN)

def double_decrypt(m,k1,k2):
    cipher2 = DES.new(k2, DES.MODE_ECB)
    dec_msg = cipher2.decrypt(unhex(m))

    cipher1 = DES.new(k1, DES.MODE_ECB)
    return cipher1.decrypt(dec_msg)





#for k1 in all_possible_keys():
#    k1 = pad("".join(k1))
#    for k2 in all_possible_keys():
#        k2 = pad("".join(k2))
#        print(double_decrypt(flag,k1,k2))


#encripted 11->f2d066b2c18b3ffa   u nc pisemo 61 za njegovu hex vrednost

to_encrypt = b'a'
a_padded = pad(to_encrypt.decode())
d = {}

print("Encripting")
for k1 in all_possible_keys():
    k1 = pad("".join(k1))
    cipher1 = DES.new(k1, DES.MODE_ECB)
    enc = cipher1.encrypt(a_padded)
    d[enc] = k1
    
print("done")
print("Starting matching second key")
a_enc=bytes.fromhex("bc366794d9792d17")
for k2 in all_possible_keys():
    k2 = pad("".join(k2))
    cipher2 = DES.new(k2, DES.MODE_ECB)
    dec = cipher2.decrypt(a_enc)
    if dec in d:
        k1=d[dec]
        print(f"Found match ke1={k1} key2={k2}")
        print(double_decrypt(flag,k1,k2))
    
