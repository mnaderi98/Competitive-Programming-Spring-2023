n = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]


def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low


for i in range(1, n):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    else:
        idx = binary_search(LIS, A[i])
        LIS[idx] = A[i]
print(len(LIS))
