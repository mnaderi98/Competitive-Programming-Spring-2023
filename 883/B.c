#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main()
{
    int t;
    scanf("%d", &t);
    getchar();

    for (int testcase = 0; testcase < t; testcase++)
    {
        char board[3][4];
        for (int i = 0; i < 3; i++)
        {
            fgets(board[i], sizeof(board[i]), stdin);
            board[i][strlen(board[i]) - 1] = '\0';
        }

        bool crossWon = false;
        bool noughtWon = false;
        bool plusWon = false;

        for (int i = 0; i < 3; i++)
        {
            if (strcmp(board[i], "XXX") == 0)
            {
                crossWon = true;
            }
            else if (strcmp(board[i], "OOO") == 0)
            {
                noughtWon = true;
            }
            else if (strcmp(board[i], "+++") == 0)
            {
                plusWon = true;
            }
        }

        for (int i = 0; i < 3; i++)
        {
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] == 'X')
            {
                crossWon = true;
            }
            else if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] == 'O')
            {
                noughtWon = true;
            }
            else if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] == '+')
            {
                plusWon = true;
            }
        }

        if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] == 'X') ||
            (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] == 'X'))
        {
            crossWon = true;
        }
        else if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] == 'O') ||
                 (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] == 'O'))
        {
            noughtWon = true;
        }
        else if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] == '+') ||
                 (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] == '+'))
        {
            plusWon = true;
        }

        if (crossWon)
        {
            printf("X\n");
        }
        else if (noughtWon)
        {
            printf("O\n");
        }
        else if (plusWon)
        {
            printf("+\n");
        }
        else
        {
            printf("DRAW\n");
        }
    }

    return 0;
}
