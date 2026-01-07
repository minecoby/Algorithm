#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a, ans = 0;
	string B;
	cin >> a;
	cin >> B;
	reverse(B.begin(), B.end());
	for(auto b : B) {
		cout << a*(b - '0') << "\n";
	}
	reverse(B.begin(), B.end());
	cout << a*stoi(B);
	return 0;
}