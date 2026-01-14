#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	float N, score, max_score, sum_score = 0;
	cin >> N;
	vector<float> scores(N);
	for(int i = 0; i < N; i++){
		cin >> score;
		scores[i] = score;
	}
	max_score = *max_element(scores.begin(), scores.end());
	for(int i = 0; i < N; i++) sum_score += scores[i] / max_score * 100;
	cout << sum_score / N;
	return 0;
}