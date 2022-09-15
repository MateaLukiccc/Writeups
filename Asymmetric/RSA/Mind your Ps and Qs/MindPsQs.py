from Crypto.Util.number import inverse, long_to_bytes

#Decrypt my super sick RSA:

c= 861270243527190895777142537838333832920579264010533029282104230006461420086153423

n= 1311097532562595991877980619849724606784164430105441327897358800116889057763413423

e= 65537

#using factordb.com we can calculate factors of n because n=p*q
#factordb is a database of factorised numbers

p= 1955175890537890492055221842734816092141

q= 670577792467509699665091201633524389157003


phi = (p-1)*(q-1)

d = pow(e, -1, phi)          #private key modular inverse of e 

m = pow(c,d,n)

print(long_to_bytes(m))