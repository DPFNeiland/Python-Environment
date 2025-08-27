#include <bits/stdc++.h>

using namespace std;

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'

typedef long long ll;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;

int N, K;
vector<int> h;

const int MAX = 1e5+10;

int memo[MAX];

int dp(int i) {
    if (i == 0) return 0;
    if(memo[i] != -1) return memo[i];

    int ret = INF;
    for(int j = max(0, i-K); j < i; j++)
        ret = min(ret, dp(j) + abs(h[j] - h[i]));

    return memo[i] = ret;
} 

int main() {

    cin >> N >> K;
    h.resize(N);
    for(int& i : h) cin >> i;

    memset(memo, -1, sizeof memo);

    cout << dp(N-1) << endl;

    return 0;

}