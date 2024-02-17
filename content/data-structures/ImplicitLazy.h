/**
 * Author: Samarth Upadhya
 * Date: 2024-02-16
 * Description: Implicit range sum segment tree with lazy prop. Bounds are [inclusive, inclusive] for the ranges.
 * Time: O(log(n)) updates; O(log(n)) queries
 * Status: Not tested
 */

struct node {
    ll lo, hi, md;
    ll val, delta;
    node *l = nullptr, *r = nullptr;
    node(ll blt, ll trt) {
        lo = blt; hi = trt;
        val = delta = 0;
        md = ((lo + hi) >> 1);
    }
    void check() {
        if (l == nullptr) {
            l = new node(lo, md);
            r = new node(md+1, hi);
        }
    }
    void update(ll blt, ll trt, ll add) {
        if(blt > hi || trt < lo) return;
        if(lo >= blt && hi <= trt) return void(delta += add);
        check(); prop();
        l->update(blt, trt, add); r->update(blt, trt, add);
        val = l->value() + r->value();
    }
    void prop() {
        l->delta += delta; r->delta += delta;
        delta = 0;
    }
    ll value() {
        return val + delta*(hi-lo+1);
    }
    ll query(ll blt, ll trt) {
        if(blt > hi || trt < lo) return 0;
        if(lo >= blt && hi <= trt) return value();
        check(); prop();
        val = l->value() + r->value();
        return l->query(blt, trt) + r->query(blt, trt);
    }
};
