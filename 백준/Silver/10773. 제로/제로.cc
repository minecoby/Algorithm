#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int K;
	cin >> K;
	stack<int> A;

	for(int i = 0; i < K; i++){
		int value;
		cin >> value;
		if(value == 0) A.pop();
		else A.push(value);
	}
	int result = 0;
	while(!A.empty()){
		result += A.top();
		A.pop();
	}
	cout << result;
	return 0;
}