#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string S;
	cin >> S;

	int time = 0;

	for (char s : S) {
        if (s >= 'A' && s <= 'C') time += 3;      
        else if (s >= 'D' && s <= 'F') time += 4; 
        else if (s >= 'G' && s <= 'I') time += 5; 
        else if (s >= 'J' && s <= 'L') time += 6; 
        else if (s >= 'M' && s <= 'O') time += 7; 
        else if (s >= 'P' && s <= 'S') time += 8; 
        else if (s >= 'T' && s <= 'V') time += 9; 
        else if (s >= 'W' && s <= 'Z') time += 10; 
    }
	cout << time;
	
	return 0;
}