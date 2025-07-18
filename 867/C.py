def min_operations(s):
    n = len(s)
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    max_freq = max(freq)
    num_max_freq = freq.count(max_freq)
    if num_max_freq == n:
        return 0
    elif num_max_freq == 1:
        max_idx = freq.index(max_freq)
        left = s.find(chr(ord('a') + max_idx))
        right = s.rfind(chr(ord('a') + max_idx))
        return max(left, n - right - 1, n - max_freq)
    else:
        return n - max_freq

t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_operations(s))
