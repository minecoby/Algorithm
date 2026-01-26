#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string S;
	getline(cin, S);

	int ans = 0;
	bool inWord = false; 

    for (int i = 0; i < S.length(); i++) {
        if (S[i] != ' ') { 
            if (!inWord) {
                ans++;
                inWord = true;
            }
        } else {
            inWord = false;
        }
    }
	cout << ans;
	return 0;
}

