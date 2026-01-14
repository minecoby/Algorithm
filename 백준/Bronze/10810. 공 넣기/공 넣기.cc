#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, M, start, end, value;
	cin >> N >> M;
	vector<int> v(N+1,0);
	for(int i = 0; i < M; i++){
		cin >> start >> end >> value;
		for(int j = start-1; j <= end-1; j++){
			v[j] = value;
		}
	}
	for(int i = 0; i < N; i++) cout << v[i] << " ";
	return 0;
}