#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	vector<int> v(10);
	vector<int> mod(42);
	for(int i = 0; i < 10; i++){
		int n;
		cin >> n;
		v[i] = n;
	}
	for(int i = 0; i < 10; i++){
		mod[v[i]%42] = 1;
	}
	
	int ans = 0;
	for(auto value: mod){
		if(value == 1) ans++;
	}
	cout << ans;
	return 0;
}