#include <bits/stdc++.h>
#define endl "\n"
#define int long long
#define mod_ 1000000007
#define fastIO                    \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
using namespace std;

const int N = 2e5 + 10;
int A[N];
vector<int> G[N];
int x;

void make(int node, int p) {
    for (auto ch : G[node]) {
        if (ch == p) {
            continue;
        }
        A[ch] = x + 1;
        while (A[ch] != A[node] + 1 && (A[ch] % 2 != A[node] % 2 || A[ch] - A[node] == 2)) {
            ++A[ch];
        }
        x = A[ch];
        make(ch, node);
    }
}

void pixel() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        G[i].clear();
    }
    x = 1;
    for (int i = 1; i < n; ++i) {
        int u, v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    A[1] = 1;
    make(1, 0);
    for (int i = 1; i <= n; ++i) {
        cout << A[i] << " ";
    }
    cout << endl;
}

int32_t main() {
    fastIO;
    int t = 1;
    cin >> t;
    while (t--) {
        pixel();        
    }
    return 0;
}





/*
 _____ _____ _____ _____ _____ 
|     |  _  |   __|   __|     |
|   --|     |__   |__   |-   -|
|_____|__|__|_____|_____|_____|

*/