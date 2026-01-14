#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	vector<int> students(31,0);
	int n;
	for(int i = 0; i < 28; i++){
		cin >> n;
		students[n] = 1;
	}
	for(int i = 1; i <= 30; i++){
		if(students[i] == 0) cout << i << "\n";
	}
	return 0;
}