#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int ans = 0, T;
	cin >> T;

	string S;
	cin >> S;

	for(char s : S) ans += s-'0';
	cout << ans;
	return 0;
}