t = int(input())

for _ in range(t):
    board = []
    m = 3
    for i in range(m):
        board.append(input())
    C = False
    N = False
    P = False

    for i in range(m):
        if board[i] == "XXX":
            C = True
        elif board[i] == "OOO":
            N = True
        elif board[i] == "+++":
            P = True

    for i in range(m):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            C = True
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            N = True
        elif board[0][i] == board[1][i] == board[2][i] == "+":
            P = True

    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        C = True
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        N = True
    elif (board[0][0] == "+"and board[1][1] == "+" and board[2][2] == "+") or (board[0][2] == "+" and board[1][1] == "+" and board[2][0] == "+"):
        P = True

    if C:
        print("X")
    elif N:
        print("O")
    elif P:
        print("+")
    else:
        print("DRAW")
