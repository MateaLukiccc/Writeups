fib = [1, 1]
for i in range(2, 11):
    fib.append(fib[i - 1] + fib[i - 2])
    
print(fib)

flag="10000100100 10010000010 10010001010 10000100100 10010010010 10001000000 10100000000 10000100010 00101010000 10010010000 00101001010 10000101000 10000010010 00101010000 10010000000 10000101000 10000010010 10001000000 00101000100 10000100010 10010000100 00010101010 00101000100 00101000100 00101001010 10000101000 10100000100"

flagBlocks=flag.split(" ")

for x in flagBlocks:
    sum=0
    for i in range(len(x)):
        if x[i]=="1":
            sum+=fib[10-i]
    print(chr(sum),end="",flush=True)