#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string A,B;
	cin >> A >> B;
	
	reverse(A.begin(), A.end());
	reverse(B.begin(), B.end());

	int ans_a = stoi(A);
	int ans_b = stoi(B);

	if(ans_a > ans_b) cout << ans_a;
	else cout << ans_b;
	


	return 0;
}