n, score = map(int, input().split())
answer = input()
for i in range(n):
    if answer[i] == 'x' and score != 0:
        score -= 1
    if answer[i] == 'o':
        score += 1
print(score)
