from pwn import xor

p="Cacturne-Grass-Dark"
key=b'kz\xc6\xb9\xd9Du\xcb\x8a\x9e\xe0\x9d\xbeo\xee\x03\xcf\xddd'

key=b'(\x1b\xa5\xcd\xac6\x1b\xae\xa7\xd9\x92\xfc\xcd\x1c\xc3G\xae\xaf\x0f'


p="Altaria-Dragon-Flying"
enc=b'iw\xd1\xac\xde_z\x83\xe3\xab\xf3\x9b\xa2r\xee\x01\xc2\xd6f\xfb\xeb'
key=b'(\x1b\xa5\xcd\xac6\x1b\xae\xa7\xd9\x92\xfc\xcd\x1c\xc3G\xae\xaf\x0f\x95\x8c'

p="Bellsprout-Grass-Poison"
enc=b'j~\xc9\xa1\xdfFi\xc1\xd2\xad\xbf\xbb\xbf}\xb04\x83\xff`\xfc\xff\xd4\xa7'
key=b'(\x1b\xa5\xcd\xac6\x1b\xae\xa7\xd9\x92\xfc\xcd\x1c\xc3G\xae\xaf\x0f\x95\x8c\xbb\xc9'

flag=b'1n53cu2357234mc1ph32'

def encrypt(plain):
	return b''.join((x ^ y) for (x,y) in zip(plain,key))


print(xor(p,enc))


f=open(r"/home/matea/CryptoHack/Crypto on the Web/pasaswords.txt","r")
words = [w.strip() for w in f.readlines()]


for i in words:
    print(xor(i,key))
    
#we just kept xoring everything until we got the flag each time knowing different name from the list