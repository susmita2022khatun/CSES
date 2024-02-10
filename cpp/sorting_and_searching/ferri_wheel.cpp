#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int n, weight;
    cin >> n >> weight;
    int ans=0;
    bool have_gondola_yet[n] = {false};
    int p[n];
    for(int i=0; i<n; i++)
        cin >> p[i];
    
    sort(p, p+n);
    int i=0;
    int j = n-1;
    while (i < j) {
        if (p[i] + p[j] > weight) {
            --j;
        } else {
            ++ans;
            have_gondola_yet[i] = have_gondola_yet[j] = true;
            ++i;
            --j;
        }
    }
    for (int i = 0; i < n; ++i) {
        ans += !have_gondola_yet[i];
    }
    cout << ans << "\n";
    return 0;
}
