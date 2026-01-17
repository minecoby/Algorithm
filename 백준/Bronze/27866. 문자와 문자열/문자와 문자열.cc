#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string S;
	int i;
	cin >> S >> i;
	cout << S[i-1];
	return 0;
}