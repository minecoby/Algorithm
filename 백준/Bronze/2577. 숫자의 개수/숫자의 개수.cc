#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int A, B, C, value;
	cin >> A >> B >> C;

	value = A * B * C;
	vector<int> numbers(10,0);
	while(value != 0){
		int cur = value % 10;
		numbers[cur] += 1;
		value /= 10;
	}
	for(auto n : numbers) cout << n << "\n";
	return 0;
}