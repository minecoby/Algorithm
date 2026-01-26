#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	vector<int> V(26, -1);
	string S;
	cin >> S;
	int index = 0;
	for(char s : S){
		if(V[s-'a'] == -1) V[s-'a'] = index;
		index++;
	}
	for(auto v : V) cout << v << " ";
	return 0;
}