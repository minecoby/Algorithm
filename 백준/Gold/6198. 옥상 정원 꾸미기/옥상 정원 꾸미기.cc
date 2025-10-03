#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;

	long long cnt = 0;
	stack<int> S;
	
	while(n--){
		int height;
		cin >> height;
		while(!S.empty() && height >= S.top()){
			S.pop();
		}
		cnt += S.size();
		S.push(height);
	}
	cout << cnt;
	return 0;
}