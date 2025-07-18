#include <stdio.h>
#include <string.h>

int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        char s[100];
        scanf("%s", s);
        char check = '0';

        for (int i = 0; i < strlen(s); i++)
        {
            if (s[i] == '?')
            {
                s[i] = check;
            }
            else
            {
                check = s[i];
            }
        }

        printf("%s\n", s);
    }

    return 0;
}
