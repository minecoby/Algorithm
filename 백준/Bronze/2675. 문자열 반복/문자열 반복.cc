#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int T, R;
	string S;
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> R >> S;
		for(auto s: S){
			for(int j = 0; j < R; j++) cout << s;
		}
		cout << "\n";
	}

	return 0;
}