def f(x):
    return len(str(x))


def binary_search(arr, l, r, x, level):
    if r >= l:
        mid = l + (r - l) // 2
        if level == 1 and arr[mid] == x \
                or level == 2 and f(arr[mid]) == x \
                or level == 3 and f(f(arr[mid])) == x:
            return mid
        elif level == 1 and arr[mid] > x \
                or level == 2 and f(arr[mid]) > x \
                or level == 3 and f(f(arr[mid])) > x:
            return binary_search(arr, l, mid-1, x, level)
        else:
            return binary_search(arr, mid + 1, r, x, level)
    else:
        return -1


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    step, i = 0, 0
    while i != len(a):
        mid = binary_search(b, 0, len(a) - 1, a[i], 1)
        if mid != -1:
            b.pop(mid)
            a.pop(i)
        else:
            i += 1

    i = 0
    while i != len(a):
        mid = binary_search(b, 0, len(a) - 1, f(a[i]), 1)
        if mid == -1:
            mid = binary_search(b, 0, len(a) - 1, a[i], 2)
        if mid != -1:
            b.pop(mid)
            a.pop(i)
            step += 1
        else:
            i += 1

    i = 0
    while i != len(a):
        mid = binary_search(b, 0, len(a) - 1, f(a[i]), 2)
        if mid != -1:
            b.pop(mid)
            a.pop(i)
            step += 2
        else:
            i += 1

    i = 0
    while i != len(a):
        mid = binary_search(b, 0, len(a) - 1, f(f(a[i])), 1)
        if mid == -1:
            mid = binary_search(b, 0, len(a) - 1, a[i], 3)
        if mid != -1:
            b.pop(mid)
            a.pop(i)
            step += 2
        else:
            i += 1

    i = 0
    while i != len(a):
        mid = binary_search(b, 0, len(a) - 1, f(f(a[i])), 2)
        if mid == -1:
            mid = binary_search(b, 0, len(a) - 1, f(a[i]), 3)
        if mid != -1:
            b.pop(mid)
            a.pop(i)
            step += 3
        else:
            i += 1

    step += 4 * len(a)
    print(step)
