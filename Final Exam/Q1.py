n = int(input())
a = list(map(int, input().split()))
mydict = {}
for i in range(n):
    if a[i] not in mydict:
        mydict[a[i]] = 1
    else:
        mydict[a[i]] += 1
sorted_dict = sorted(mydict.items(), key = lambda x:x[1])
n_ghermez = n//2
j = 0
gh = 0
abi = 0
#nobat ghermez = FAlse
nobat = True
m = n
i = 0
while (i<len(sorted_dict)):
    if nobat:
        sorted_dict[i] = (sorted_dict[i][0], sorted_dict[i][1]-1)
        abi+=1
        nobat = False
        i += 1

    else:
        sorted_dict[i] = (sorted_dict[i][0], sorted_dict[i][1]-1)
        nobat = True
        if sorted_dict[i][1] == 0:
            i += 1
print(abi)
