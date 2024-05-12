/**
 * Author: Samarth Upadhya
 * Date: 2024-03-15
 * Description: Ordered Statistic Tree that can store multiple elements at the same time
 * Time: O(log(n)) key order, O(log(n)) insert and erase
 * Status: Tested
 */

#include <bits/extc++.h>
using namespace __gnu_pbds;

struct multiost {
    typedef tree<
        pii,
        null_type,
        less<pii>,
        rb_tree_tag,
        tree_order_statistics_node_update
    > ost;

    ost s;
    unsigned cnt = 0;

    multiost() = default;
    multiost(initializer_list<int> l) { for(int x : l) insert(x); }
    void insert(int x) { s.insert({x, cnt++}); }
    ost::iterator find_by_order(int k) { return s.find_by_order(k); }
    int order_of_key(int k) { return s.order_of_key({k, 0}); }
    void erase(int x) {
        auto it = s.lower_bound({x, 0});
        // erase(it); // erases only first element
        while(it != s.end() && it->first == x) erase(it++); // erases all elements
    }
    void erase(ost::iterator it) { s.erase(it); }
    size_t size() const { return s.size(); }
};

