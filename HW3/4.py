n = int(input())
homes = input()
s, t = sorted(map(int, input().split()))
s -= 1
t -= 1
operation = 0

i = s + 1
while i < t:
    if homes[i] == "H":
        HH = 1
        while i + 1 < t and homes[i + 1] == "H":
            HH += 1
            i += 1 
        operation += bin(HH).count('1')
    i += 1
print(operation)