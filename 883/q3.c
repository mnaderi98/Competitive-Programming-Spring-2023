#include <stdio.h>
#include <stdlib.h>

#define ll long long

ll m = 1000000007;

ll binpow(ll a, ll b)
{
    if (b == 0)
        return 1;

    ll res = binpow(a, b / 2);

    if (b % 2)
        return ((res % m) * (res % m) * a) % m;
    else
        return (res % m) * (res % m) % m;
}

int sortbyCond(const void *a, const void *b)
{
    ll first_a = ((const ll(*)[2])a)[0][0];
    ll first_b = ((const ll(*)[2])b)[0][0];

    ll second_a = ((const ll(*)[2])a)[0][1];
    ll second_b = ((const ll(*)[2])b)[0][1];

    if (first_a != first_b)
        return (first_a < first_b) ? -1 : 1;
    else
        return (second_a > second_b) ? -1 : 1;
}

int main()
{
    ll T;
    scanf("%lld", &T);

    for (ll iii = 0; iii < T; iii++)
    {
        ll n, m, h, x;
        scanf("%lld %lld %lld", &n, &m, &h);

        ll new_values[n][2];
        ll pp, ppx;

        for (ll i = 0; i < n; i++)
        {
            ll v[m];

            for (ll j = 0; j < m; j++)
            {
                scanf("%lld", &x);
                v[j] = x;
            }

            qsort(v, m, sizeof(ll), sortbyCond);

            ll ans = 0, s = 0;
            ll j;

            for (j = 0; j < m; j++)
            {
                s += v[j];
                ans += s;

                if (s > h)
                    break;
            }

            if (j == m)
                j--;

            if (s > h)
            {
                j--;
                ans -= s;
            }

            new_values[i][0] = j;
            new_values[i][1] = ans;

            if (i == 0)
            {
                pp = j;
                ppx = ans;
            }
        }

        qsort(new_values, n, sizeof(new_values[0]), sortbyCond);

        ll final = 0;

        for (ll i = 0; i < n; i++)
        {
            final++;

            if (new_values[i][0] == pp && new_values[i][1] == ppx)
                break;
        }

        printf("%lld\n", final);
    }

    return 0;
}
