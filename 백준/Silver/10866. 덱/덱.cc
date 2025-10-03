#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;

	deque<int> D;

	while(n--){
		string cmd;
		cin >> cmd;

		if(cmd == "push_front"){
			int value;
			cin >> value;

			D.push_front(value);
		}

		if(cmd == "push_back"){
			int value;
			cin >> value;

			D.push_back(value);
		}

		if(cmd == "pop_front"){
			if(D.empty()) {
				cout << -1 << "\n";
			} else {
				cout << D.front() << "\n";
				D.pop_front();
			}
		}

		if(cmd == "pop_back"){
			if(D.empty()) {
				cout << -1 << "\n";
			} else {
				cout << D.back() << "\n";
				D.pop_back();
			}
		}

		if(cmd == "size"){
			cout << D.size() << "\n";
		}

		if(cmd == "empty"){
			if(D.empty()) cout << 1 << "\n";
			else cout << 0 << "\n";
		}

		if(cmd == "front"){
			if(D.empty()) cout << -1 << "\n";
			else cout << D.front() << "\n";
		}

		if(cmd == "back"){
			if(D.empty()) cout << -1 << "\n";
			else cout << D.back() << "\n";
		}
		
	}
	return 0;
}