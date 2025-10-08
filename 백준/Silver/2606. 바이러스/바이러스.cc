#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[105];
bool vis[105];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n,m;
	cin >> n;
	cin >> m;

	while(m--){
		int a,b;
		cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	int cnt = 0;
	queue<int> q;
	q.push(1);
	vis[1] = true;

	while(!q.empty()){
		int cur = q.front(); q.pop();
		for(auto index : adj[cur]){
			if(vis[index]) continue;
			vis[index] = true;
			cnt++;
			q.push(index);
		}
	}
	cout << cnt;
	return 0;
}