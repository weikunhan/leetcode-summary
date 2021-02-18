# Union-Find

The following questions, I prefer to solve by using Union-Find. It may have the optimal method, please check the discussion in LeetCode.  

* [Graph](##Graph)
* [2D Array](##2D-Array)

## Graph

In computer science, a disjoint-set data structure, also called a union–find data structure or merge–find set, is a data structure that stores a collection of disjoint (non-overlapping) sets. Equivalently, it stores a partition of a set into disjoint subsets. It provides operations for adding new sets, merging sets (replacing them by their union), and finding a representative member of a set. The last operation allows to find out efficiently if any two elements are in the same or different sets. [Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

This type of problem includes: find connections problem, find minimum cost problem

The time complexity of the union-find is (log*(n)).

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 261 | https://leetcode.com/problems/graph-valid-tree/ | |
| 323 | https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/ | |
| 1135 | https://leetcode.com/problems/connecting-cities-with-minimum-cost/ | |
| 1135* | https://leetcode.com/discuss/interview-question/356981 | [this link](../practice/amazon/min_cost_to_connect_all_nodes.py) |
| 1135* | https://leetcode.com/discuss/interview-question/357310 | [this link](../practice/amazon/min_cost_to_repair_edges.py) |

## 2D Array

By using a hash table, some 2D array question can use union-find to solve.

This type of problem includes: find share points problem

The time complexity of the union-find is (log*(n)).

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 305 | https://leetcode.com/problems/number-of-islands-ii/ | [this link](../practice/solution/0305_number_of_islands_ii.py) |
| 547 | https://leetcode.com/problems/friend-circles/ | |
| 721 | https://leetcode.com/problems/accounts-merge/ | [this link](../practice/solution/0721_accounts_merge.py) |
| 737 | https://leetcode.com/problems/sentence-similarity-ii/ | |
| 924 | https://leetcode.com/problems/minimize-malware-spread/ | [this link](../practice/solution/0924_minimize_malware_spread.py) | 
| 947 | https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/ | |
| 1202 | https://leetcode.com/problems/smallest-string-with-swaps/ | [this link](../practice/solution/1202_smallest_string_with_swaps.py) |
