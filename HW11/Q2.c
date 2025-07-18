#include <stdio.h>
#include <math.h>

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);

    int a[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    int block_size = (int)sqrt(n);
    int blocks[(int)(n / block_size) + 1];

    int b = -1;
    int c = 0;
    while (c < n)
    {
        if (c % block_size == 0)
        {
            b += 1;
        }
        blocks[b] += a[c];
        c += 1;
    }

    for (int i = 0; i < q; i++)
    {
        int op, l, r;
        scanf("%d %d %d", &op, &l, &r);
        if (op == 1)
        {
            int res = 0;
            while (l - 1 % block_size != 0 && l - 1 < r)
            {
                res += a[l - 1];
                l += 1;
            }
            while (l - 1 + block_size - 1 < r)
            {
                res += blocks[(l - 1) / block_size];
                l += block_size;
            }
            while (l - 1 < r)
            {
                res += a[l - 1];
                l += 1;
            }
            printf("%d\n", res);
        }
        else if (op == 2)
        {
            blocks[(int)(l - 1) / block_size] += (r - a[l - 1]);
            a[l - 1] = r;
        }
    }

    return 0;
}
