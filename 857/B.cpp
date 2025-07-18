#include <iostream>
#include <vector>
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
        vector<int> b(n);

        for (int j = 0; j < n; j++)
        {
            cin >> b[j];
        }

        int aviaries = 0;
        int ones = 0;
        int extra = 0;

        for (int j = 0; j < n; j++)
        {
            if (b[j] == 1)
            {
                ones++;
                if (extra > 0)
                {
                    extra--;
                }
                else
                {
                    aviaries++;
                }
            }
            else if (b[j] == 2)
            {
                int need = (ones + 1) / 2;
                extra = max(0, aviaries - need);
            }
            else
            {
                throw invalid_argument("Invalid day value: " + to_string(b[j]));
            }
        }

        cout << aviaries << endl;
    }

    return 0;
}