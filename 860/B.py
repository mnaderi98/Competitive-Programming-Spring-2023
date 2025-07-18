for _ in range(int(input())):
    m = int(input())
    participants = [[] for _ in range(m)]
    winners = [-1] * m
    used = set()

    for i in range(m):
        n = int(input())
        participants[i] = list(map(int, input().split()))

        # check if there is only one participant on day i
        if n == 1:
            winners[i] = participants[i][0]
            used.add(winners[i])

    # loop over the remaining days
    for i in range(m):
        if winners[i] != -1:
            continue  # we already have a winner for day i

        possible_winners = set(participants[i]) - used
        if not possible_winners:
            print(-1)
            break  # no solution exists

        winner = possible_winners.pop()
        winners[i] = winner
        used.add(winner)

    else:
        print(*winners)
