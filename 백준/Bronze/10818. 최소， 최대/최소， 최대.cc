#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n,value;
	cin >> n;
	vector<int> v(n);
	for(int i = 0; i < n; i++){
		cin >> value;
		v[i] = value;
	}
	cout << *min_element(v.begin(),v.end()) << " " << *max_element(v.begin(),v.end());

	return 0;
}