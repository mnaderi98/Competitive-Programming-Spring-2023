#include <bits/stdc++.h>

using namespace std;

#define int long long

void init()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
}

int mod = 1e9 + 7;

vector<int> a[100005];

int d[100005], vis[100005], maxd = 0, d2[100005];

void dfs(int x)
{
    vis[x] = 1;
    for (auto it : a[x])
    {
        if (vis[it])
            continue;
        d[it] = d[x] + 1;
        if (d[it] > d[maxd])
            maxd = it;
        dfs(it);
    }
}

void dfs2(int x)
{
    vis[x] = 1;
    for (auto it : a[x])
    {
        if (vis[it])
            continue;
        d2[it] = d2[x] + 1;
        if (d2[it] > d2[maxd])
            maxd = it;
        dfs2(it);
    }
}

void solve()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        vis[i] = 0;
    for (int i = 1; i <= n; i++)
        d[i] = 0;
    for (int i = 1; i <= n; i++)
        d2[i] = 0;
    maxd = 0;
    for (int i = 1; i < n; i++)
    {
        int u, v;
        cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }
    dfs(1);
    for (int i = 1; i <= n; i++)
        vis[i] = 0;
    dfs2(maxd);
    for (int i = 1; i <= n; i++)
        vis[i] = 0;
    d[maxd] = 0;
    dfs(maxd);
    for (int i = 1; i <= n; i++)
    {
        d[i] = max(d[i], d2[i]);
    }
    sort(d + 1, d + n + 1);
    stack<int> s;
    int res = n - 1;
    for (int i = n; i >= 1; i--)
    {
        while (d[res] >= i)
        {
            res--;
        }
        s.push(res + 1);
    }
    while (!s.empty())
    {
        cout << s.top() << " ";
        s.pop();
    }
    cout << "\n";
}

signed main()
{
    init();
    int tt = 1;
    while (tt--)
    {
        solve();
    }
    return 0;
}