import sys

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# create dictionary to store satisfaction increases from eating certain dishes together
d = {}
for _ in range(k):
    x, y, c = map(int, input().split())
    d[(x, y)] = c

# initialize dp table with -1 for all states (bitmasks of eaten dishes)
dp = [[-1 for _ in range(n)] for _ in range(1 << n)]

# base case: dp[2^i][i] = a[i] for all i (eating one dish)
for i in range(n):
    dp[1 << i][i] = a[i]

# loop through all possible bitmasks
for mask in range(1, 1 << n):
    # loop through all possible dishes in the current bitmask
    for i in range(n):
        # if the current dish is not in the current bitmask, skip it
        if not (mask & (1 << i)):
            continue
        # loop through all possible dishes to eat before the current dish
        for j in range(n):
            # if the dish to eat before the current dish is not in the current bitmask, skip it
            if not (mask & (1 << j)):
                continue
            # if the dish to eat before the current dish is the current dish, skip it
            if i == j:
                continue
            # if eating the dishes in this order is not allowed, skip it
            if (j+1, i+1) not in d:
                continue
            # update dp table with the maximum satisfaction for the current bitmask and current dish
            dp[mask][i] = max(dp[mask][i], dp[mask ^ (1 << i)]
                              [j] + a[i] + d[(j+1, i+1)])

# find maximum satisfaction from eating m dishes
ans = 0
for mask in range(1, 1 << n):
    # count number of dishes eaten in the current bitmask
    count = 0
    for i in range(n):
        if mask & (1 << i):
            count += 1
    # if the number of dishes eaten is m, update maximum satisfaction
    if count == m:
        for i in range(n):
            if dp[mask][i] != -1:
                ans = max(ans, dp[mask][i])

print(ans)
