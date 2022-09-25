fib = [1, 1]
for i in range(2, 11):
    fib.append(fib[i - 1] + fib[i - 2])



def c2f(c):
    n = ord(c)
    b = ''
    for i in range(10, -1, -1):
        if n >= fib[i]:
            n -= fib[i]
            b += '1'
        else:
            b += '0'
    return b

flag = "corctf{b4s3d_4nd_f1bp!113d}"
enc = ''
for c in flag:
    enc += c2f(c) + ' '
print(enc)