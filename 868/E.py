t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    s = list(s)  # convert string to a list of characters for easy swapping
    
    left, right = 0, n-1
    swaps = 0
    
    while left < right:
        if s[left] == s[right]:
            diff_left = left + 1
            while diff_left < right and s[diff_left] == s[left]:
                diff_left += 1
            diff_right = right - 1
            while diff_right > left and s[diff_right] == s[right]:
                diff_right -= 1
            if diff_left == right and diff_right == left:
                # not possible to make the string an anti-palindrome
                swaps = -1
                break
            if diff_left == right:
                s[diff_right], s[left] = s[left], s[diff_right]
            elif diff_right == left:
                s[diff_left], s[right] = s[right], s[diff_left]
            else:
                # choose the closest different character to swap with
                if right - diff_left < diff_right - left:
                    s[diff_left], s[right] = s[right], s[diff_left]
                else:
                    s[diff_right], s[left] = s[left], s[diff_right]
            swaps += 1
        left += 1
        
        right -= 1
    
    print(swaps if swaps != -1 else -1)
