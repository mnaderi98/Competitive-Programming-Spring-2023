n = int(input())


def check_digit(n):
    s = str(n)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


while True:
    n += 1
    if check_digit(n):
        print(n)
        break
