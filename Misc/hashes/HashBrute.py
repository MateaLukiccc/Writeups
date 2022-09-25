from pwn import remote, process
from itertools import product
import string
from hashlib import sha256
from tqdm import tqdm

conn = remote("202.120.7.219", 15555)


def solve_pow():
    line = conn.recvline().decode().strip()
    print(line)
    suffix = line[14:30]
    print(suffix)
    enc=line[35:].strip()
    print(enc)
    line = conn.recvline().decode().strip()
    print(line)
    for x in tqdm(product(string.ascii_letters + string.digits + '!#$%&*-?', repeat=4)):
        s =  "".join(x)+suffix
        if sha256(s.encode()).hexdigest() == enc or len(sha256(s.encode()).hexdigest())!=len(enc):
            print("\nFINISHEDDDDDDDDD",sha256(s.encode()).hexdigest())
            conn.sendline("".join(x).encode())
            break
    
solve_pow()   
line = conn.recvline().decode().strip()
print(line)
line = conn.recvline().decode().strip()
print(line)
line = conn.recvline().decode().strip()
print(line)
line = conn.recvline().decode().strip()
print(line)


