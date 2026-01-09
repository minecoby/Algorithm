#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int H,M;
	cin >> H >> M;
	M = M - 45;
	if(M < 0){
		M = M + 60;
		H--;
		if(H < 0) H = H + 24;
	}
	cout << H << " " << M;
	return 0;
}