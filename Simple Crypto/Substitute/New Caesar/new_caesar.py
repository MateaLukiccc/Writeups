import string

LOWERCASE_OFFSET = ord("a")         #97
ALPHABET = string.ascii_lowercase[:16]   #abcdefghijklmnop

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET   #since flag is b16 encoded it can also be [0,15]
	t2 = ord(k) - LOWERCASE_OFFSET   #[0,15]
	return ALPHABET[(t1 + t2) % len(ALPHABET)]   

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1            #key is of length 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])      #key[i%len(key)]=key[0]
print(enc)

