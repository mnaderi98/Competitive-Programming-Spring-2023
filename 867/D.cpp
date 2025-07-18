#include <bits/stdc++.h>
using namespace std;

const int INF = 2e9;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> l(n), r(n);
        for (int i = 0; i < n; i++)
        {
            cin >> l[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> r[i];
        }

        vector<int> diff(n);
        diff[0] = r[0] - l[0] + 1;
        for (int i = 1; i < n; i++)
        {
            diff[i] = r[i] - l[i] + 1 - (l[i] - r[i - 1] - 1);
        }

        int ans = INF;
        int black = 0;
        int right = 0;
        for (int left = 0; left < n; left++)
        {
            while (right < n && black < k)
            {
                black += diff[right];
                right++;
            }
            if (black >= k)
            {
                ans = min(ans, r[right - 1] - l[left] + 1);
            }
            black -= diff[left];
        }

        if (ans == INF)
        {
            cout << "-1\n";
        }
        else
        {
            cout << ans << "\n";
        }
    }
    return 0;
}
