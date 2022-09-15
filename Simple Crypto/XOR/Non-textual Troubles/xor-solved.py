from random import seed, randrange


seed(True, version=2)

#with open("plaintext.txt", "r") as read, open("ciphertext.txt", "w") as write:
plaintext = "blub"

for i in range(33):
    print(randrange(256))
    

print("finished")

B=[68,
32,
130,
60,
253,
230,
241,
194,
107,
48,
249,
14,
199,
221,
1,
228,
136,
117,
52,
162,
15,
11,
13,
4,
195,
110,
216,
14,
113,
224,
253,
119,
176]

plaintext="◄aÁh»ö☼o:¥ì6Ñ×↓kT:4▲¡9↓ÐEÍ"

for i,char in enumerate("aÁh»öo:¥ì6Ñ×kT:4¡9ÐEÍ"):
    A = ord(char)
    ciphertext=chr(A ^ B[i])
    print(ciphertext)


#UACTF{b4d_h4b175_l34d_70_py7h0n2}
