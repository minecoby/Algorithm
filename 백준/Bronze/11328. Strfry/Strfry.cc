#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	for(int i = 0; i < N; i++){
		vector<int> alpha(27, 0);
		string a, b;
		bool check = true;
		cin >> a >> b;

		for(auto s: a) alpha[s-97] += 1;
		for(auto s: b) alpha[s-97] -= 1;
		for(int i = 0; i < 27; i++) if(alpha[i] != 0) check = false;
		if(check) cout << "Possible" << "\n"; else cout << "Impossible" << "\n";
	}
	
	return 0;
}