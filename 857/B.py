t = int(input())
for _ in range(t):
    n = int(input())

    b = list(map(int, input().split()))

    if 2 not in b:
        print(len(b))
    elif 1 not in b:
        print(0)

    else:
        feut = 0
        maximum = 0
        ghafas = 0
        for j in b:
            if j == 1:
                feut += 1
                if maximum <= 0:
                    ghafas += 1

                else:
                    maximum -= 1

            elif j == 2:
                minimum = int(feut / 2) + 1
                maximum = max(0, ghafas - minimum)

        print(ghafas)
