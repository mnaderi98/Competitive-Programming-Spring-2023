n = int(input())
a = list(map(int, input().split()))
mmm = max(a)
index = a.index(mmm)
res = 0
less_after = n - index - 1
less_before = n - less_after - 1
res += (less_after * less_before)
a.remove(mmm)
while(len(a) > 2):
    mmm = max(a)
    n -= 1
    index = a.index(mmm)
    less_after = n - index - 1
    less_before = n - less_after - 1
    res += (less_after * less_before)
    a.remove(mmm)
print(res)
    
