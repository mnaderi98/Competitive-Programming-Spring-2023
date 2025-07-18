s = input()
if len(s) == 0:
    print(0)
try:
    m = s.count('0')
    n = s.count('1')
    print(min(m, n) * 2)
except:
    print(0)
