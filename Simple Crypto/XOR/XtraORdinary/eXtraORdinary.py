from random import randint

with open('flag.txt', 'rb') as f:                  #otvara flag iz fajla i cuva ga u promeljivoj
    flag = f.read()

with open('secret-key.txt', 'rb') as f:            #cita kljuc iz fajla i cuva ga u promenljivoj
    key = f.read()

def encrypt(ptxt, key):                           #xor-uje dve promeljive i vraca rezultat
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

ctxt = encrypt(flag, key)                         #ctxt je xor izmedju kluca i flaga   (ctxt=flag^key)

random_strS = [                                   #niz stringova od kojih se neki ponavljaju
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]

for random_str in random_strS:                    #za svaki string se obrne oko milion for petlji i xoruje ili ne xoruje ctxt sa tim stringom ako 
    for i in range(randint(0, pow(2, 8))):        #je broj loopova neparan on ce biti xorovan ako je paran nece
        for j in range(randint(0, pow(2, 6))):
            for k in range(randint(0, pow(2, 4))):
                for l in range(randint(0, pow(2, 2))):
                    for m in range(randint(0, pow(2, 0))):
                        ctxt = encrypt(ctxt, random_str)
                        
                        


with open('output.txt', 'w') as f:
    f.write(ctxt.hex())
    
#57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637