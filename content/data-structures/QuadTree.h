/**
 * Author: Samarth Upadhya
 * Date: 2024-02-12
 * Description: Implicit count inversions quad tree with lazy prop. Bounds are [inclusive, inclusive] with the bottom lowest borner and top right corner of the query box.
 * Time: O(n+m)
 * Status: Not tested
 */

struct node {
    array<ll, 2> bl, tr, mid;
    ll val, delta;
    node *q1 = nullptr, *q2 = nullptr, *q3 = nullptr, *q4 = nullptr;
    node(array<ll, 2> blt, array<ll, 2> trt) {
        bl = blt; tr = trt;
        val = delta = 0;
        mid = {(bl[0] + tr[0]) >> 1, (bl[1] + tr[1]) >> 1};
    }
    void check() {
        if (q1 == nullptr) {
            q1 = new node({mid[0] + 1, mid[1] + 1}, tr);
            q2 = new node({bl[0], mid[1] + 1}, {mid[0], tr[1]});
            q3 = new node(bl, mid);
            q4 = new node({mid[0] + 1, bl[1]}, {tr[0], mid[1]});
        }
    }
    void update(array<ll, 2> blt, array<ll, 2> trt) {
        if ((blt[0] > tr[0] || blt[1] > tr[1]) ||
            (trt[0] < bl[0] || trt[1] < bl[1])) return;
        if ((blt[0] <= bl[0] && blt[1] <= bl[1]) &&
            (trt[0] >= tr[0] && trt[1] >= tr[1])) return void(delta++);
        check(); prop();
        q1->update(blt, trt); q2->update(blt, trt);
        q3->update(blt, trt); q4->update(blt, trt);
        val = q1->value() + q2->value() + q3->value() + q4->value();
    }
    void prop() {
        q1->delta += delta; q2->delta += delta;
        q3->delta += delta; q4->delta += delta;
        delta = 0;
    }
    ll value() {
        ll tot = (tr[1] - bl[1] + 1) * (tr[0] - bl[0] + 1);
        if (delta & 1) return tot - val;
        return val;
    }
    ll query(array<ll, 2> blt, array<ll, 2> trt) {
        if ((blt[0] > tr[0] && blt[1] > tr[1]) ||
            (trt[0] < bl[0] && trt[1] < bl[1])) return 0;
        if ((blt[0] <= bl[0] && blt[1] <= bl[1]) ||
            (trt[0] >= tr[0] && trt[1] >= tr[1])) return value();
        prop();
        val = q1->value() + q2->value() + q3->value() + q4->value();
        return q1->query(blt, trt) + q2->query(blt, trt) +
               q3->query(blt, trt) + q4->query(blt, trt);
    }
};
