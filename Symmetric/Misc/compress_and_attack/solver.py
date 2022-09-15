from pwn import *
import string

r = remote("mercury.picoctf.net", 2431)
valid_chars=string.ascii_letters+string.digits+"_}"
solutiion_so_far="picoCTF{"

while "}" not in solutiion_so_far:
    best=""
    best_len=999
    for c in valid_chars:
        try:
            r.recvuntil("encrypted:")
            r.sendline(solutiion_so_far+c)
            r.recvline()
            r.recvline()
            length=int(r.recvline().decode().rstrip())
            if length < best_len:
                best=c
                best_len=length
        except:
            r=remote("mercury.picoctf.net", 2431)
    solutiion_so_far+=best
    print(solutiion_so_far)
