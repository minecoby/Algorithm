#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n,m;
	cin >> n >> m;
	int board[102][102];
	bool visited[102][102];
	int weight[102][102];

	int dx[4] = {1,0,-1,0};
	int dy[4] = {0,1,0,-1};
	for(int i = 0; i < n; i++){
		string row;
		cin >> row; 
		for(int j = 0; j < m; j++){
			board[i][j] = row[j] - '0'; 
		}
	}

	queue<pair<int, int> > Q;
	Q.push({0,0});
	visited[0][0] = 1;
	weight[0][0] = 1;
	while(!Q.empty()){
		pair<int,int> cur = Q.front(); Q.pop();
		for(int i = 0; i < 4; i++){
			int nx = cur.first + dx[i]; int ny = cur.second + dy[i];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if(board[nx][ny] == 1 && !visited[nx][ny]){
				visited[nx][ny] = 1;
				weight[nx][ny] = weight[cur.first][cur.second] + 1;
				Q.push({nx,ny});
			}
		}
	}
	cout << weight[n-1][m-1];
	return 0;
}