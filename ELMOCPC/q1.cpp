#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <assert.h>
using namespace std;

long long readInt(char endd, long long l, long long r)
{
    bool is_neg = false;
    long long result = 0;
    int nums = 0;
    int flag = -1;

    while (true)
    {
        char g = getchar();
        if (g == '-')
        {
            assert(flag == -1);
            is_neg = true;
            continue;
        }
        if ('0' <= g && g <= '9')
        {
            result *= 10;
            result += g - '0';
            if (nums == 0)
            {
                flag = g - '0';
            }
            nums++;
            assert(flag != 0 || nums == 1);
            assert(flag != 0 || is_neg == false);

            assert(!(nums > 19 || (nums == 19 && flag > 1)));
        }
        else if (g == endd)
        {
            assert(nums > 0);
            if (is_neg)
            {
                result = -result;
            }
            if (!(l <= result && result <= r))
            {
                cerr << l << " " << r << " " << result << endl;
            }
            assert(l <= result && result <= r);

            return result;
        }
        else
        {
            assert(false);
        }
    }
}

set<pair<int, int>> hh;

struct p
{
    long long x, y, t;
};
bool operator<(p a, p b)
{
    if (a.x == b.x)
    {
        return a.y < b.y;
    }
    return a.x < b.x;
}
p arr[200200];

long long cross(long long x1, long long y1, long long x2, long long y2)
{
    return x1 * y2 - x2 * y1;
}

long long is_left(p a, p b, p c)
{
    return cross(b.x - a.x, b.y - a.y, c.x - b.x, c.y - b.y) > 0;
}
long long is_right(p a, p b, p c)
{
    return cross(b.x - a.x, b.y - a.y, c.x - b.x, c.y - b.y) < 0;
}

p upper[200200];
p lower[200200];
p pol[200200];
int up = 0, lw = 0, pn = 0;
int T;
int n;
int m;
int main()
{
    T = readInt('\n', 1, 10);
    for (int iii = 0; iii < T; iii++)
    {
        hh.clear();
        n = readInt(' ', 0, 100000);
        m = readInt('\n', 1, 100000);
        up = lw = 0;
        for (int i = 0; i < n; i++)
        {
            int x, y;
            x = readInt(' ', -1000000000, 1000000000);
            y = readInt('\n', -1000000000, 1000000000);
            assert(hh.count(make_pair(x, y)) == 0);
            hh.insert(make_pair(x, y));
            arr[i].x = x;
            arr[i].y = y;
            arr[i].t = 1;
        }
        for (int i = 0; i < m; i++)
        {
            int x, y;
            x = readInt(' ', -1000000000, 1000000000);
            y = readInt('\n', -1000000000, 1000000000);
            assert(hh.count(make_pair(x, y)) == 0);
            hh.insert(make_pair(x, y));
            arr[n + i].x = x;
            arr[n + i].y = y;
            arr[n + i].t = 2;
        }
        sort(arr, arr + n + m);
        for (int i = 0; i < n + m; i++)
        {
            if (arr[i].t == 2)
            {
                i = i;
            }
            while (up >= 2 && !is_right(upper[up - 2], upper[up - 1], arr[i]))
            {
                up--;
            }
            while (lw >= 2 && !is_left(lower[lw - 2], lower[lw - 1], arr[i]))
            {
                lw--;
            }
            upper[up++] = arr[i];
            lower[lw++] = arr[i];
        }
        bool all_police = true, all_theif = true;
        for (int i = 0; i < up; i++)
        {
            if (upper[i].t == 1)
                all_theif = false;
        }
        for (int i = 0; i < lw; i++)
        {
            if (lower[i].t == 1)
                all_theif = false;
        }
        if (all_theif)
        {
            cout << 3 << endl;
            continue;
        }
        up = lw = 0;
        for (int i = 0; i < n + m; i++)
        {
            if (arr[i].t == 2)
            {
                i = i;
            }
            while (up >= 2 && is_left(upper[up - 2], upper[up - 1], arr[i]))
            {
                up--;
            }
            while (lw >= 2 && is_right(lower[lw - 2], lower[lw - 1], arr[i]))
            {
                lw--;
            }
            upper[up++] = arr[i];
            lower[lw++] = arr[i];
        }
        for (int i = 0; i < up; i++)
        {
            if (upper[i].t == 2)
                all_police = false;
        }
        for (int i = 0; i < lw; i++)
        {
            if (lower[i].t == 2)
                all_police = false;
        }
        if (all_police)
        {
            cout << 0 << endl;
            continue;
        }
        pn = 0;
        for (int i = 0; i < up - 1; i++)
        {
            pol[pn++] = upper[i];
        }
        for (int i = lw - 1; i >= 1; i--)
        {
            pol[pn++] = lower[i];
        }
        bool found = false;
        int cur = 0;
        for (int i = 0; i < pn; i++)
        {
            if (pol[i].t != 1)
            {
                if (cur == i)
                {
                    cur = (cur + 1) % pn;
                }
                continue;
            }
            while (pol[cur].t == 1)
            {
                cur = (cur + 1) % pn;
            }
            int a = (i + pn - 1) % pn, b = i, c = (cur + pn - 1) % pn, d = cur;
            p third;
            third.x = pol[a].x + (pol[c].x - pol[b].x);
            third.y = pol[a].y + (pol[c].y - pol[b].y);
            if (is_right(pol[d], pol[c], third))
            {
                found = true;
            }
            if (cur == i)
            {
                cur = (cur + 1) % pn;
            }
        }
        if (found)
        {
            cout << 1 << endl;
        }
        else
        {
            cout << 2 << endl;
        }
    }
    assert(getchar() == -1);
}