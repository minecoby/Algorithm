#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[1005];
bool vis[1005];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n,m;
	cin >> n >> m;
	while(m--){
		int a,b;
		cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}

	int num = 0;
	for(int i = 1; i <= n; i++){
		if(vis[i]) continue;
		num++;
		queue<int> q;
		q.push(i);

		while (!q.empty())
		{
			int cur = q.front(); q.pop();
			for(auto index : adj[cur]){
				if(vis[index]) continue;
				vis[index] = true;
				q.push(index);
			}
		}
		
	}
	cout << num;
	return 0;
}