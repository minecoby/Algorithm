#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int N, K, S, Y, ans = 0;
	cin >> N >> K;
	vector<vector <int>> woman_v(7, vector<int>(2,0));
	vector<vector <int>> man_v(7, vector<int>(2,0));

	for(int i = 0; i < N; i++){
		cin >> S >> Y;
		if(S == 0){
			if(woman_v[Y][1] == 0) woman_v[Y][0]++;
			woman_v[Y][1]++;
			if(woman_v[Y][1] == K) woman_v[Y][1] = 0;
		}
		else{
			if(man_v[Y][1] == 0) man_v[Y][0]++;
			man_v[Y][1]++;
			if(man_v[Y][1] == K) man_v[Y][1] = 0;
		}
	}
	for(int i = 1; i <= 6; i++){
		ans += woman_v[i][0];
		ans += man_v[i][0];
	}

	cout << ans;
	return 0;
}