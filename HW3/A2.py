import math
n = int(input())

if n >= 2:
    numbers = [0] * (n+1)
    numbers[0] = 1
    numbers[1] = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if numbers[i] == 0:
            # از آی ضرب در آی شروع کردیم چون آی ضربدر همه ی اعداد اول کمتر از آن قبلا به عنوان عدد غیر اول درنظر گرفته شده
            j = i * i
            while(j < n + 1):
                numbers[j] = 1
                j += i

    result = numbers.count(0)

    print(result)

else:
    print(0)
