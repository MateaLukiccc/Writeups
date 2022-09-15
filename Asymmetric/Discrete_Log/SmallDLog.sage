from Crypto.Util.number import long_to_bytes

p= int("8c5378994ef1b",16)
g=int("02",16)

A= int("269beb3b0e968",16)
B=int("4757336da6f70",16)

g = Mod(g,p)
m = discrete_log(A,g)
n = discrete_log(B,g)
print(long_to_bytes(m))
print(long_to_bytes(m))
#CTFlearn{H3ll0_Fr13nd}