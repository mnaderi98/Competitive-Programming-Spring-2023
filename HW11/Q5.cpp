#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    for (int i = 0; i < q; i++)
    {
        int op, l, r;
        cin >> op >> l >> r;

        if (op == 1)
        {
            int result = 0;
            int prev = 0;
            l = l - 1;

            for (int j = l; j < r; j++)
            {
                prev = min(prev + a[j], a[j]);
                result = min(result, prev);
            }

            cout << result << endl;
        }
        else if (op == 2)
        {
            a[l - 1] = r;
        }
    }

    return 0;
}
