#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, M, i, j;
	cin >> N >> M;
	vector<int> v(N+1);
	for(int index = 0; index < N; index++) v[index] = index+1;
	
	for(int index = 0; index < M; index++){
		cin >> i >> j;
		i -= 1; j -= 1;
		int temp = v[i];
		v[i] = v[j];
		v[j] = temp;
	}
	for(int index = 0; index < N; index++) cout << v[index] << " ";
	return 0;
}