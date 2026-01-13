#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int X, N, a, b, ans = 0;
	cin >> X >> N;

	for(int i = 0; i < N; i++){
		cin >> a >> b;
		ans += a*b;
	}
	if(X == ans) cout << "Yes"; else cout << "No";
	return 0;
}