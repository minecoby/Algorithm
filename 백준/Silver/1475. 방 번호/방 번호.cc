#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	vector<int> numbers(10,1);
	int ans = 1; string s;

	cin >> s;
	for(auto value: s){
		int num = value - '0';
		//6또는 9가 아닐 때 
		if(num != 6 && num != 9){
			if(numbers[num] == 0){
				ans += 1;
				for(int i = 0; i < 10; i++) numbers[i] += 1;
				 numbers[num] -= 1;
			}
			else numbers[num] -= 1;
		}
		//6또는 9일 때 
		else{
			if(numbers[num] != 0) numbers[num] -= 1;
			else if(numbers[9] != 0) numbers[9] -= 1;
			else if(numbers[6] != 0) numbers[6] -= 1;
			else{
				ans += 1;
				for(int i = 0; i < 10; i++) numbers[i] += 1;
				numbers[num] -= 1;
			}
			
		}
	}
	cout << ans;
	return 0;
}