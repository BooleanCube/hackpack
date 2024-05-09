/**
 * Author: Samarth Upadhya
 * Date: 2024-05-08
 * Description: Fast array-based bottom-up segment tree for cheesers. 0-indexed and intervals are [inclusive, inclusive].
 * Time: O(log(n)) updates; O(log^2(n)) queries
 * Status: Tested
 */

struct segtree {
    int n;
    vl tree, lazy, lupd;
    vector<pii> rng;
    segtree(int N) : n(N) {
        tree = vl(n<<1), lazy = vl(n<<1), lupd = vl(n<<1);
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
    ll _value(int idx, ll val) {
        return val * (rng[idx].s - rng[idx].f + 1);
    }
    void incUpdate(int l, int r, ll val) { _incUpdate(l+n, r+n, val); }
    void _incUpdate(int l, int r, ll val) {
        if(l == r) {
            _updateLupd(l, _value(l, val));
            return void(lazy[l] += val);
        }
        if(l & 1) {
            lazy[l] += val;
            _updateLupd(l, _value(l, val));
            return void(_incUpdate(l+1, r, val));
        }
        if(!(r & 1)) {
            lazy[r] += val;
            _updateLupd(r, _value(r, val));
            return void(_incUpdate(l, r-1, val));
        }
        return _incUpdate(l>>1, r>>1, val);
    }
    void _updateLupd(int idx, ll val) {
        while(idx) {
            lupd[idx] += val;
            idx >>= 1;
        }
    }
    ll query(int l, int r) {
        return _queryLazy(l+n, r+n, 0) + _querySeg(l+n, r+n, 0) + _queryLupd(l+n, r+n, 0);
    }
    ll _queryLazy(int l, int r, ll t) {
        ll idx = (l&1 ? l : r), cnt = 0;
        if((l==r) || (l&1) || !(r&1)) {
            while(idx > 1) {
                idx >>= 1;
                cnt += lazy[idx];
            }
        }
        if(l == r) return _value(l, cnt) + t;
        if(l & 1) return _queryLazy(l+1, r, t + _value(l, cnt));
        if(!(r & 1)) return _queryLazy(l, r-1, t + _value(r, cnt));
        return _queryLazy(l>>1, r>>1, t);
    }
    ll _querySeg(int l, int r, ll t) {
        if(l == r) return tree[l] + t;
        if(l & 1) return _querySeg(l+1, r, t + tree[l]);
        if(!(r & 1)) return _querySeg(l, r-1, t + tree[r]);
        return _querySeg(l>>1, r>>1, t);
    }
    ll _queryLupd(int l, int r, ll t) {
        if(l == r) return lupd[l] + t;
        if(l & 1) return _queryLupd(l+1, r, t + lupd[l]);
        if(!(r & 1)) return _queryLupd(l, r-1, t + lupd[r]);
        return _queryLupd(l>>1, r>>1, t);
    }
    void printtree() {
        for(ll i : lazy) cout << i << " ";
        cout << endl;
    }
};
