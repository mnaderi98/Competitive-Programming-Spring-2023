n = int(input())

good = 1
# xa + xb = n
#n = x(a+b)
# if gcd(a,b) == 1:
#   gcd(xa, xb) = x
#n % x == 1
# کافیست بزرگترین مقسوم علیه ان پیدا شود.

for i in range(2, int(n/2) + 1):
    if n % i == 0:
        good = int(n/i)
        break

print(good, n-good)
