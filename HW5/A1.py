s = input()
dp1 = [0] * (len(s)+2)
dp2 = [0] * (len(s)+2)

for i in range(1, len(s)+1):
    dp1[i] = dp1[i-1]
    dp2[len(s)-i-1] = dp2[len(s)-i]
    if s[i-1].islower():
        dp1[i] += 1
    if s[len(s)-i].isupper():
        dp2[len(s)-i-1] += 1

final = [dp2[k] + dp1[k] for k in range(0, len(s))]
print(min(final))
