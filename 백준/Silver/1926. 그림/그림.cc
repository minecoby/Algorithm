#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n,m;
	cin >> n >> m;
	int board[502][502];
	bool visited[502][502];
	int dx[4] = {1,0,-1,0};
	int dy[4] = {0,1,0,-1};
	int cnt = 0;
	int max_paint = 0;

	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			cin >> board[i][j];
		}
	}

	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(board[i][j] == 1 && !visited[i][j]){
				cnt++;
				queue<pair<int,int> > Q;
				Q.push({i,j});
				visited[i][j] = 1;
				int area = 1;

				while(!Q.empty()){
					pair<int,int> cur = Q.front(); Q.pop();
					for(int k = 0; k < 4; k++){
						int nx = cur.first + dx[k]; int ny = cur.second + dy[k];
						if(board[nx][ny] == 1 && !visited[nx][ny]){
							visited[nx][ny] = 1;
							area++;
							Q.push({nx,ny});
						}
					}
				max_paint = max(max_paint, area);
				}
			}
		}
	}
	cout << cnt << "\n" << max_paint;
	return 0;
}