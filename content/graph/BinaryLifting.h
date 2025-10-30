/**
 * Author: Samarth Upadhya
 * Date: 2025-10-29
 * Description: Binary Lifting for LCA and distance of 2 nodes on a tree rooted at index 0.
 * Time: Ө(log^2(n)) LCA, Ө(log(n)) kth, Ө(nlog(n)) construction
 * Status: Tested
 */

struct BL {
  int n, L;
  vi ht;
  vector<vi> jmp;
  BL(int N, vi &P) : n(N), L(__lg(N)+1) {
    jmp = vector<vi>(N, vi(L)); ht = vi(N);
    rep(i, 0, n) jmp[i][0] = P[i], climb(P, i);
    rep(j, 1, L) rep(i, 0, n) jmp[i][j] = jmp[jmp[i][j-1]][j-1];
  }
  int climb(vi &p, int u) {
    if(!u) return 0;
    if(ht[u]) return ht[u];
    return ht[u] = climb(p, p[u]) + 1;
  }
  int kth(int u, int k) {
    while(k) {
      u = jmp[u][__builtin_ctz(k)];
      k -= k & -k;
    }
    return u;
  }
  int lca(int u, int v, int k = 1) {
    if(ht[v] < ht[u]) swap(u, v);
    if(ht[u] < ht[v]) return lca(u, kth(v, ht[v] - ht[u]));
    if(u == v) return u;
    while(kth(u, 1LL<<k) != kth(v, 1LL<<k)) k++; k--;
    return lca(kth(u, 1LL<<k), kth(v, 1LL<<k));
  }
  int dist(int u, int v) { return ht[u] + ht[v] - ht[lca(u, v)]; }
};
