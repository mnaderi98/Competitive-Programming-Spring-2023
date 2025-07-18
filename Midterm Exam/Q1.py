n = int(input())
board = []
for i in range(n):
    board.append(input())
row = 0
col = 0
horses = 0


def check_adjs(row, col):
    x = True
    if 0 <= col+1 < n and 0 <= row + 2 < n and board[row + 2][col + 1] == "A":
        return False
    if 0 <= col-1 < n and 0 <= row + 2 < n and board[row + 2][col + -1] == "A":
        return False
    if 0 <= col+1 < n and 0 <= row - 2 < n and board[row - 2][col + 1] == "A":
        return False
    if 0 <= col-1 < n and 0 <= row - 2 < n and board[row - 2][col - 1] == "A":
        return False
    if 0 <= col+2 < n and 0 <= row + 1 < n and board[row + 1][col + 2] == "A":
        return False
    if 0 <= col+2 < n and 0 <= row - 1 < n and board[row - 1][col + 2] == "A":
        return False
    if 0 <= col-2 < n and 0 <= row + 1 < n and board[row + 1][col - 2] == "A":
        return False
    if 0 <= col-2 < n and 0 <= row - 1 < n and board[row - 1][col - 2] == "A":
        return False
    return True


def count_hourses(r=0, c=0, nums=0):

    if nums == 0:
        return board

    for i in range(r, n):
        if i == r:
            x = c

        else:
            x = 0
        for j in range(x, n):
            if board[row][col] != "#" and check_adjs(i, j):

                board[i, j] = board[i][:j] + "A" + board[i][j+1:]
                out = count_hourses(i, j+2, nums+1)
                if out is not None:
                    return out
                board[i] = board[i][:j] + "." + board[i][j+1:]
    return None


out = count_hourses(r=0, c=0, nums=0)
for _ in board:
    print(_)
