/**
 * Author: Samarth Upadhya
 * Date: 2025-10-17
 * Description: Intuitive network flow algorithm by traversing all augmenting paths
 * Time: Ө(E * F) where F represents the max flow
 * Status: Tested
 */

struct FordFulkerson {
    const int n, s, t;
    vector<vi> adj, cap;
    FordFulkerson(int N, int S, int T) : n(N), s(S), t(T) {
        adj = vector<vi>(n);
        cap = vector<vi>(n, vi(n));
    }
    void addEdge(int u, int v, int w) {
        adj[u].push_back(v);
        adj[v].push_back(u);
        cap[u][v] += w;
    }
    int bfs(vi &par) {
        fill(all(par), -1); par[s] = -2;
        deque<pair<int, int>> q; q.push_back({s, INF});
        while (!q.empty()) {
            auto [u, w] = q.front(); q.pop_front();
            for (int v : adj[u]) {
                if(par[v] != -1 || cap[u][v] == 0) continue;
                par[v] = u;
                int flow = min(w, cap[u][v]);
                if(v == t) return flow;
                q.push_back({v, flow});
            }
        }
        return 0;
    }
    int calc() {
        int flow = 0, cur = 0; vi par(n);
        while(cur = bfs(par)) {
            flow += cur; int v = t;
            while(v != s) {
                int u = par[v];
                cap[u][v] -= cur;
                cap[v][u] += cur;
                v = u;
            }
        }
        return flow;
    }
};
