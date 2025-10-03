#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	int cnt = 1;
	stack<int> S;
	string ans;
	while(n--){
		int value;
		cin >> value;
		while(cnt <= value){
			S.push(cnt++);
			ans += "+\n";
		}
		if(S.top() != value){
			cout << "NO\n";
			return 0;
		}
		S.pop();
		ans += "-\n";
	}
	cout << ans;
	return 0;
}