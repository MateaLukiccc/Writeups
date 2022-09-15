numbers= [16, 9, 3 ,15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
flag=[]

for number in numbers:
    flag.append(chr(number+96))          #chr is reverse of ord function

print("".join(flag))    #list to string 
