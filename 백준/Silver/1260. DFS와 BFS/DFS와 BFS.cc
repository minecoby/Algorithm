#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[1005];
bool vis_bfs[1005];
bool vis_dfs[1005];

void dfs(int cur){
  vis_dfs[cur] = true;
  cout << cur << ' ';
  for(auto nxt : adj[cur]){
    if(vis_dfs[nxt]) continue;    
    dfs(nxt);
  }
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n,m,v;
	cin >> n >> m >> v;
	while(m--){
		int a,b;
		cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	for(int i = 1; i <= n; i++) sort(adj[i].begin(), adj[i].end());
	vector<int> bfs_ans;
	vector<int> dfs_ans;

	//bfs
	queue<int> q;
	q.push(v);
	vis_bfs[v] = true;
	while(!q.empty()){
		int cur = q.front(); q.pop();
		bfs_ans.push_back(cur);
		for(auto index: adj[cur]){
			if(vis_bfs[index]) continue;
			vis_bfs[index] = true;
			q.push(index);
		}
	}
	
	//dfs
	dfs(v);

	cout << "\n";
	for(auto ans: bfs_ans) cout << ans << " ";
	return 0;
}