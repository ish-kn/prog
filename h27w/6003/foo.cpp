#include<bits/stdc++.h>
using namespace std;

#define N (1<<26) // 2^26
#define ull unsigned long long 
 
ull DP[N + 1];
int s = 1;

ull g(int n) {
    for (int i = s; i <= n; i++) {
        DP[i] = (1103515245 * DP[i - 1] + 12345) % N;
        s = i + 1;
    }
    return DP[n];
}

int calc_gk(int n) {
    int k = 1;
    while (1) {
        if (g(n + k) == g(n)) return k;
        k++;
    }
}
    
int main() {
    memset(DP, -1, sizeof(DP));
    DP[0] = 1;
    
    cout << N << endl;
    cout << g(2) << endl;
    cout << g(3) << endl;
    cout << calc_gk(0) << endl;
        
    return 0;
}
