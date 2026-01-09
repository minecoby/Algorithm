#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int A, B, time;
	cin >> A >> B >> time;
	B = B + time;
	if(B >= 60){
		A = A + B/60;
		B = B%60;
		if(A > 23) A = A-24;
	}
	cout << A << " " << B;
	return 0;
}