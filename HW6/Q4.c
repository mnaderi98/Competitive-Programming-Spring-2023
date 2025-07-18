#include <stdio.h>

#define MOD 1000000007

int main()
{
    int n, q;
    scanf("%d", &n);
    long a[n + 1];
    for (int i = 1; i <= n; i++)
    {
        scanf("%ld", &a[i]);
    }
    scanf("%d", &q);
    while (q--)
    {
        int s, k;
        scanf("%d %d", &s, &k);
        long sum = 0;
        int p = s;
        while (p <= n)
        {
            sum += a[p];
            p += k;
        }
        printf("%ld\n", sum);
    }
    return 0;
}
