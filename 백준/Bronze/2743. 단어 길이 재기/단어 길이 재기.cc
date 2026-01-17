#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int ans = 0;
	string S;
	cin >> S;
	for(auto s : S) ans++;
	cout << ans;
	return 0;
}