#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string a,b;
	int ans = 0;
	cin >> a >> b;
	vector<int> count_a(27,0);
	vector<int> count_b(27,0);

	for(auto e: a) count_a[e-97] += 1;
	for(auto e: b) count_b[e-97] += 1;

	for(int i = 0; i < 27; i++) ans += abs(count_a[i] - count_b[i]);
	cout << ans;
	return 0;
}