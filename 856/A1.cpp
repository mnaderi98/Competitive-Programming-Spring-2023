#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        string list[n];
        for (int j = 0; j < n; j++)
        {
            cin >> list[j];
        }

        sort(list, list + n, [](string a, string b)
             { return a.length() > b.length(); });
        string a0 = list[0];
        string a1 = list[1];

        string s;
        if (a0.substr(1) == a1.substr(0, a1.length() - 1))
        {
            s = a0 + a1[a1.length() - 1];
        }
        else
        {
            s = a1 + a0[a0.length() - 1];
        }

        if (s != string(s.rbegin(), s.rend()))
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
    }

    return 0;
}