import math
n, k = map(int, input().split())
result = 0
for i in range(k-1):
    if i == 0:
        result += math.factorial(n)//(math.factorial(n-i-2)
                                      * math.factorial(i+2))
    if i == 1:
        result += math.factorial(n)//(math.factorial(n-i-2)
                                      * math.factorial(i+2)) * 2
    if i == 2:
        result += math.factorial(n)//(math.factorial(n-i-2)
                                      * math.factorial(i+2)) * 9

print(result+1)
