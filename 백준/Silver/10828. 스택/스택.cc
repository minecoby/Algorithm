#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	string cmd;
	int value;
	stack<int> A;

	for(int i = 0; i < N; i++){
		cin >> cmd;
		if(cmd == "push"){
			cin >> value;
			A.push(value);
		}
		if(cmd == "top"){
			if(A.size()) cout << A.top() << "\n";
			else cout << -1 << "\n";
		}
		if(cmd == "size") cout << A.size() << "\n";
		if(cmd == "empty"){
			if(A.size()) cout << 0 << "\n";
			else cout << 1 << "\n";
		}
		if(cmd == "pop"){
			if(A.size()){
				cout << A.top() << "\n";
				A.pop();
			}
			else cout << -1 << "\n";
		}
	}
	return 0;
}