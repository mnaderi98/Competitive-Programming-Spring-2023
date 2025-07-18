#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n), b(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> b[i];
        }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        bool flag = false;
        for (int i = 0; i < n; i++)
        {
            if (a[i] <= b[i])
            {
                cout << 0 << endl;
                flag = true;
                break;
            }
        }
        if (!flag)
        {
            vector<int> counter(n, 0);
            for (int i = 0; i < n; i++)
            {
                int ax = a[i];
                int j = 0;
                while (j < n && b[j] < ax)
                {
                    counter[i] += 1;
                    j += 1;
                }
            }
            int result = 1;
            int k = 0;
            sort(counter.begin(), counter.end());
            for (int x = 0; x < n; x++)
            {
                result = (result * ((counter[x] - k) % MOD)) % MOD;
                k += 1;
            }
            cout << result % MOD << endl;
        }
    }
    return 0;
}
