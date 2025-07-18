import math
n, m = map(int, input().split())
numerator = math.factorial(n+(2*m)-1)
denumerator = (math.factorial(2*m)*math.factorial(n-1))
result = numerator//denumerator
print(int(result) % (1000000007))
