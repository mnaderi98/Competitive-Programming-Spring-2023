n, x, k = map(int, input().split())
channels = []
for i in range(n):
    channels.append(input())
new = (x + k) % n
print(channels[new - 1])
