/**
 * Author: Samarth Upadhya
 * Date: 2024-05-08
 * Description: Fast array-based bottom-up segment tree for cheesers. 0-indexed and intervals are [inclusive, inclusive].
 * Time: O(log(n)) updates; O(log^2(n)) queries
 * Status: Tested
 */

struct segtree {
    int n;
    vl tree, lazy;
    vector<pii> rng;
    segtree(int N) : n(N) {
        tree = vl(n<<1), lazy = vl(n<<1);
        rng = vector<pii>(n<<1);
        rng[0] = _construct(1);
    }
    pii _construct(int idx) {
        if(idx >= n) return rng[idx] = {idx-n, idx-n};
        int ch = idx << 1; // left child
        pii lh = _construct(ch);
        pii rh = _construct(ch+1);
        return rng[idx] = {lh.f, rh.s};
    }
    ll value(int idx, ll val) { return val * (rng[idx].s - rng[idx].f + 1); }
    void incUpdate(int l, int r, ll val) { _incUpdate(l+n, r+n, val); }
    void _incUpdate(int l, int r, ll val) {
        for(;l<r; l>>=1,r>>=1) {
            if(l & 1) { _updateLazy(l, val); lazy[l++] += val; }
            if(l == r) break;
            if(!(r & 1)) { _updateLazy(r, val); lazy[r--] += val; }
        }
        _updateLazy(l, val); lazy[l] += val;
    }
    void _updateLazy(int idx, ll val) { for(val=value(idx, val); idx; idx>>=1) tree[idx] += val; }
    ll query(int l, int r) { return _queryTree(l+n, r+n); }
    ll _queryTree(int l, int r, ll t = 0) {
        for(;l<r; l>>=1,r>>=1) {
            if(l & 1) { t += value(l, _climbLazy(l)) + tree[l]; l++; }
            if(l == r) break;
            if(!(r & 1)) { t += value(r, _climbLazy(r)) + tree[r]; r--; }
        }
        return value(l, _climbLazy(l)) + tree[l] + t;
    }
    ll _climbLazy(int idx, ll cnt = 0) { for(idx>>=1; idx; idx>>=1) cnt += lazy[idx]; return cnt; }
};
