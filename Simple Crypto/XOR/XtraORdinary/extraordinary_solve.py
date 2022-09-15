import binascii
from random import randint

def encrypt(ptxt, key):
    ctxt = b''
    ptxt=binascii.unhexlify(ptxt)
    key=binascii.unhexlify(key)
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt
#--------Data--------#

c = bytes.fromhex("57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637")

#--------XOR--------#

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

while True:
    for random_str in random_strs:                                     #prolazi kroz sve kombinarcije enkriptovanja sa stringom
        for m in range(randint(0, 1)):
            c = encrypt(c.hex(), random_str.hex())

    flag_prefix = b"picoCTF{"                                          #prefiks flag-a
    key = encrypt(c[:len(flag_prefix)].hex(), flag_prefix.hex())
    if key.decode().isprintable():
        print(key," ",len(key))
        key = b'Africa!'                                                #zasto nije afrika!a jer se key ponavlja ide afrika!afika...
        flag = encrypt(c.hex(), key.hex())
        if flag.startswith(b"picoCTF{"):
            print(flag)
            exit(0)
   
       