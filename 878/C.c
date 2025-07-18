#include <iostream>
#include <algorithm>
#include <vector>

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
            vector<int> counter(n);
            for (int i = 0; i < n; i++)
            {
                int ax = a[i];
                int j = 0;
                while (j < n && b[j] < ax)
                {
                    counter[i]++;
                    j++;
                }
            }
            long long result = 1;
            int k = 0;
            for (int x = 0; x < n; x++)
            {
                result = (result * (counter[x] - k)) % MOD;
                k++;
            }
            cout << result << endl;
        }
    }
    return 0;
}
