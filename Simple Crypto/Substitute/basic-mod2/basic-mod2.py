import string

alphabet = string.ascii_lowercase
alphabet += "0123456789_"
flag_enc = "104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377 ".split()

flag = ""
for c in flag_enc: 
    pos = pow(int(c), -1, 41)  #same as c^(-1) % 41
    flag += alphabet[pos-1]

print("picoCTF{"+flag+"}")