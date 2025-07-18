#include <stdio.h>
#include <string.h>

#define MAXN 100000

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n, q;
        char s[MAXN];
        scanf("%d %d", &n, &q);
        scanf("%s", s);
        int dp[MAXN];
        int x = 0;
        int dpSize = 0;
        while (x + 2 < n)
        {
            if (s[x] == s[x + 1] || s[x] == s[x + 2] || s[x + 1] == s[x + 2])
            {
                dp[dpSize++] = x;
            }
            x++;
        }
        dp[dpSize++] = n;
        while (q--)
        {
            int l, r;
            scanf("%d %d", &l, &r);
            int result = 0;
            while (dp[result] < l - 1)
            {
                result++;
            }
            if (dp[result] + 2 <= r - 1)
            {
                printf("YES\n");
            }
            else
            {
                printf("NO\n");
            }
        }
    }
    return 0;
}
