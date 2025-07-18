n = int(input())
a = []
for i in range(n):
    a.append(list(map(float, input().split())))
m = (1 << n) #2^n
output = [0] * m 

output[-1] = 1 #assign last element of output to 1

for i in range(m-2, 0, -1):
    p = output[i]
    for j in range(n):
        if (i & (1 << j)):
            continue
        for k in range(n):
            if not(i & (1 << k)):
                continue

            bits = bin(i)
            one_bits = bits.count('1')

            p += (2 * output[i ^ (1 << j)] * a[k][j]) / \
                (one_bits*(one_bits + 1))
    output[i] = p
for x in range(n):
    if x == n - 1:
        print(format(output[1 << x], '.6f'))
    else:
        print(format(output[1 << x], '.6f'), end=" ")
