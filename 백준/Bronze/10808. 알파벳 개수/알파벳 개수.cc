#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string s;
    cin >> s;

    for(char i = 'a'; i <= 'z'; i++){
        int count = 0;
        for(auto c: s){
            if(c == i)count++;
        }
        cout << count << " ";
    }

    return 0;
}
