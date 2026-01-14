#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	vector<int> v(8);
	int value, max_value, max_index;

	for(int i = 0; i < 9; i++){
		cin >> value;
		v[i] = value;
	}
	max_value = *max_element(v.begin(),v.end()+1);
	for(int i = 0; i < 9; i++){
		if(v[i] == max_value){
			max_index = i+1;
			break;
		}
	}
	cout << max_value << "\n" << max_index;
	return 0;
}