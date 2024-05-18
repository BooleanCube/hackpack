/**
 * Author: Samarth Upadhya
 * Date: 2024-05-08
 * Description: Fast array-based bottom-up segment tree for cheesers. 0-indexed and intervals are [inclusive, inclusive].
 * Time: Ө(log(n)) updates; Ө(log(n)) queries
 * Status: Tested
 */

template <class T>
struct segtree {
    using vt = vector<T>;
    const int n; constexpr static T def = 0;
    vt tree, lazy;
    vector<pii> rng;
    segtree(int N) : n(N) {
        tree = vt(n<<1), lazy = vt(n<<1), rng = vector<pii>(n<<1);
        rng[0] = _construct(1);
    }
    pii _construct(int idx) {
        if(idx >= n) return rng[idx] = {idx-n, idx-n};
        pii lh = _construct(idx << 1), rh = _construct((idx << 1)+1);
        return rng[idx] = {lh.f, rh.s};
    }
    T value(int idx, T val) { return val * (rng[idx].s - rng[idx].f + 1); }
    void update(int l, int r, T val) { _incUpdate(l+n, r+n, val); }
    void _incUpdate(int l, int r, T val) {
        for(;l<r; l>>=1,r>>=1) {
            if(l & 1) { _updateLazy(l, val); lazy[l++] = op(lazy[l], val); }
            if(l == r) break;
            if(!(r & 1)) { _updateLazy(r, val); lazy[r--] = op(lazy[r], val); }
        }
        _updateLazy(l, val); lazy[l] = op(lazy[l], val);
    }
    void _updateLazy(int idx, T val) { for(val=value(idx, val); idx; idx>>=1) tree[idx] = op(tree[idx], val); }
    T query(int l, int r) { return _queryTree(l+n, r+n); }
    T _queryTree(int l, int r, T t = def) {
        for(;l<r; l>>=1,r>>=1) {
            if(l & 1) { t = op(t, value(l, _climbLazy(l)), tree[l]); l++; }
            if(l == r) break;
            if(!(r & 1)) { t = op(t, value(r, _climbLazy(r)), tree[r]); r--; }
        }
        return op(value(l, _climbLazy(l)), tree[l], t);
    }
    T _climbLazy(int idx, T cnt = def) { for(idx>>=1; idx; idx>>=1) cnt = op(cnt, lazy[idx]); return cnt; }
    T op(T a, T b) { return a + b; }
    T op(T a, T b, T c) { return op(a, op(b, c)); }
};
