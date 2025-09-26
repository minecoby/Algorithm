#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	cin >> s;
	
	for(char i = 'a'; i <= 'z'; i++){
		int cnt = 0;
		for(char c : s){
			if(i == c) cnt++;
		}
		cout << cnt << " ";
	}
	return 0;
}