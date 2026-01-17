#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	string S;
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> S;
		cout << S[0] << S[S.length()-1] << "\n";
	}
	return 0;
}