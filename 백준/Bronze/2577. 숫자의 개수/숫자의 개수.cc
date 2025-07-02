#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a,b,c;
    cin >> a >> b >> c;
    int cal = a*b*c;
    vector<int> cnt(10);
    while(cal > 0){
        cnt[cal%10]++;
        cal = cal / 10;
    }
    for(auto e : cnt){
        cout << e << "\n";
    }
}