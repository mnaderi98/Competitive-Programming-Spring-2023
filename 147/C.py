t = int(input())
def reverse(start, end, arr):
    for i in range(((end - start) // 2)+1):
        tmp = arr[i+start]
        arr[i+start] = arr[end-i]
        arr[end-i] = tmp
for i in range(t):
    s = input()
    arr = list(s)
    start = 0
    end = len(s)-1
    while start < len(s) and end > -1 and end > start:
        if arr[start] == "1" and arr[end] == "0":
            reverse(start, end, arr)
        elif arr[start] == "0" and arr[end] == "1":
            start += 1
            end -= 1
        elif arr[start] == "?":
            start += 1
        elif arr[end] == "?":
            end -= 1
        elif arr[start] == arr[end] == "0":
            start += 1
        elif arr[start] == arr[end] == "1":
            end -= 1
    for i in range(len(s)):
        if arr[i] == "?" and i-1 >0 :
            arr[i] = arr[i-1]
        elif arr[i] == "?" and i+1 < len(arr):
            arr[i] = arr[i+1]
        elif arr[i] == "?":
            arr[i] = "0"

    print("".join(arr))

        