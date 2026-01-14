#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, M, start, end;
	cin >> N >> M;
	vector<int> v(N+1);
	for(int i = 1; i <= N; i++) v[i] = i;

	for(int i = 0; i < M; i++){
		cin >> start >> end;
		reverse(v.begin() + start, v.begin() + end + 1);
	}

	for(int i = 1; i <= N; i++) cout << v[i] << " ";
	return 0;
}