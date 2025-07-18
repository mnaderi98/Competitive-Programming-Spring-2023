import sys

INF = 2 * 10 ** 9

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        l = list(map(int, sys.stdin.readline().split()))
        r = list(map(int, sys.stdin.readline().split()))

        diff = [0] * n
        diff[0] = r[0] - l[0] + 1
        for i in range(1, n):
            diff[i] = r[i] - l[i] + 1 - (l[i] - r[i - 1] - 1)

        ans = INF
        black = 0
        right = 0
        for left in range(n):
            while right < n and black < k:
                black += diff[right]
                right += 1
            if black >= k:
                ans = min(ans, r[right - 1] - l[left] + 1)
            black -= diff[left]

        if ans == INF:
            print("-1")
        else:
            print(ans)

if __name__ == '__main__':
    main()
