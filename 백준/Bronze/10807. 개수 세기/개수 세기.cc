#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, a, ans;
	cin >> N;
	vector<int> v(201, 0);
	for(int i = 0; i < N; i++){
		cin >> a;
		v[a+100] += 1;
	}
	cin >> ans;
	cout << v[ans+100];
	return 0;
}