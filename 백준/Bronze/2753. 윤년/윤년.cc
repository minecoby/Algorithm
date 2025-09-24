#include <iostream>
using namespace std;
#include <bits/stdc++.h>

int main() {
	int year;
	cin >> year;
	if(year%100 != 0 && year%4 == 0 || year%400 == 0) cout << 1;
	else cout << 0;
	return 0;
}