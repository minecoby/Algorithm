#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	stack<pair<int,int>> S;
	int cnt = 1;
	while(N--){
		int value;
		cin >> value;
		while(!S.empty()){
			if(value < S.top().first){
				cout << S.top().second << " ";
				break;
			}
			S.pop();
		}
		if(S.empty()) cout << 0 << " ";
		S.push(make_pair(value,cnt++));
	}

	return 0;
}