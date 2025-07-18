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
        char res[100];
        char ques = '0';
        strcpy(res, s);

        for (int k = 0; k < strlen(s); k++)
        {
            if (s[k] == '?')
            {
                res[k] = ques;
            }
            else
            {
                ques = s[k];
            }
        }

        printf("%s\n", res);
    }

    return 0;
}
