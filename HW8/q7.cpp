#include <bits/stdc++.h>
using namespace std;
bool DFS(bool *visited, vector<vector<int>> &graph, int source)
{
    visited[source] = 1;
    for (int i = 0; i < graph[source].size(); i++)
    {
        if (visited[graph[source][i]] == 1)
            return 0;
        if (visited[graph[source][i]] == 0)
        {
            if (!DFS(visited, graph, graph[source][i]))
                return 0;
        }
    }
    return 1;
}

int main()
{
    int v, e;
    cin >> v >> e;
    vector<vector<int>> graph;
    graph.resize(v + 1);
    for (int i = 0; i < e; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
    }
    int c = 0;
    for (int i = 1; i <= v; i++)
    {
        bool visited[v + 1] = {};
        if (DFS(visited, graph, i) == 0)
        {
            cout << "No";
            return 0;
        }
    }
    cout << "Yes";
    return 0;
}
