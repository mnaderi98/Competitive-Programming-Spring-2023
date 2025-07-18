n = int(input())
A = list(map(int, input().split()))
q = int(input())
for i in range(q):
    s, k = map(int, input().split())
    ans = 0
    for j in range((n-s)//k + 1):
        ans += A[j*k+s-1]
        ans = ans % 1000000007
    print(ans)
