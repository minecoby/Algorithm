#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, X, value, ans = 0;
	cin >> N;
	vector<bool> check(2000001, false);
	vector<int> A(N);
	for(int i = 0; i < N; i++){
		cin >> value;
		A[i] = value;
	}
	cin >> X;
	for(int i = 0; i < N; i++){
		if(X-A[i] > 0 && X-A[i] <= 2000000 && check[X - A[i]]) ans++;
		check[A[i]] = true;
	}
	cout << ans;
	return 0;
}