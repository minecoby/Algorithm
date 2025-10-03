#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	queue<int> Q;
	int n;
	cin >> n;

	while(n--){
		string cmd;
		cin >> cmd;
		if(cmd == "push"){
			int value;
			cin >> value;

			Q.push(value);
		}
		if(cmd == "pop"){
			if(Q.empty()) cout << -1 << "\n";
			else{
				cout << Q.front() << "\n";
				Q.pop();
			}
		}
		if(cmd == "size") cout << Q.size() << "\n";
		if(cmd == "empty"){
			if(Q.empty()) cout << 1 << "\n";
			else cout << 0 << "\n";
		}
		if(cmd == "front"){
			if(Q.empty()) cout << -1 << "\n";
			else cout << Q.front() << "\n";
		} 
		if(cmd == "back"){
			if(Q.empty()) cout << -1 << "\n";
			else cout << Q.back() << "\n";
		} 
	}
	return 0;
} 