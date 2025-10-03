#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;

	vector<int> A;
	vector<int> result;
	stack<int> S;
	while(n--) {
		int value;
		cin >> value;
		A.push_back(value);
		result.push_back(-1);
	}
	
	for(int i = A.size()-1; i >= 0; i--){
		int t = A[i];
		while(!S.empty() && t >= S.top()){
			S.pop();
		}
		if(!S.empty()){
			result[i] = S.top();
		}
		S.push(t);
	}
	for(auto r : result) cout << r << " ";
	return 0;
}