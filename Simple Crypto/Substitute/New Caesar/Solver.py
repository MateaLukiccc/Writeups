####################################### DECODING PART ##############################################################
import string

LOWERCASE_OFFSET = ord("a")         #97
ALPHABET = string.ascii_lowercase[:16]   #abcdefghijklmnop

encrypted="dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

def unshift(c,k):
	t1 = ord(c) - LOWERCASE_OFFSET   
	t2 = ord(k) - LOWERCASE_OFFSET   
	return ALPHABET[(t1 - t2) % len(ALPHABET)]   


def b16_decode(encoded):
    dec=""
    for u in range(0,len(encoded),2):
        p1=ALPHABET.index(encoded[u])
        p2=ALPHABET.index(encoded[u+1])
        p1="{0:04b}".format(p1)
        p2="{0:04b}".format(p2)
        p=p1+p2 #they are strings so we dont need to shift bytes
        dec+=chr(int(p,2))
    return dec  

for k in ALPHABET:
	decryptedFirst=""
	for i,c in enumerate(encrypted):
		decryptedFirst+=unshift(c,k[0])
	
	print(b16_decode(decryptedFirst),k)
