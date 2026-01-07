#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	double A,B;
	cin >> A >> B;
	cout << fixed;
	cout.precision(15);
	cout << A/B;
	return 0;
}