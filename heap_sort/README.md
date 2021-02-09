# Heap Sort

The following questions, I prefer to solve by using Heap Sort. It may have the optimal method, please check the discussion in LeetCode.  

* [Min Heap](##Min-Heap)
* [Max Heap](##Max-Heap)

## Min Heap

In computer science, a heap is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C. The node at the "top" of the heap (with no parents) is called the root node. The heap is one maximally efficient implementation of an abstract data type called a priority queue, and in fact, priority queues are often referred to as "heaps", regardless of how they may be implemented. In a heap, the highest (or lowest) priority element is always stored at the root. However, a heap is not a sorted structure; it can be regarded as being partially ordered. A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority. [Wikipedia](https://en.wikipedia.org/wiki/Heap_(data_structure))

This type of problem includes: find the kth smallest problem, find the kth rare problem， find minimum cost problem

The time complexity of the min heap is Search-Min O(1), Insert O(log(n)), and Delete-Min O(log(n)). The space complexity of the min heap is O(n). 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 373 | https://leetcode.com/problems/find-k-pairs-with-smallest-sums/ | |
| 378 | https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/ | |
| 1057 | https://leetcode.com/problems/campus-bikes/ | [this link](../practice/solution/1057_campus_bikes.py) |
| 1167 | https://leetcode.com/problems/minimum-cost-to-connect-sticks/ | [this link](../practice/solution/1167_minimum_cost_to_connect_sticks.py) |
| 1167* | https://leetcode.com/discuss/interview-question/344677 | [this link](../practice/a/min_cost_to_connect_ropes.py) |
| 1481 | https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/ | [this link](../practice/solution/1481_least_number_of_unique_integers_after_k_removals.py) |   
| | https://www.1point3acres.com/bbs/thread-627760-1-1.html | [this link](../practice/others/load_balance.py) |

## Max Heap

Since Python's heapq implementation does not have built in support for max heap, we can just invert the values stored into the heap so it functions as a max heap. 

This type of problem includes: find the kth largest problem, find the kth frequently problem, find maximum profit problem

The time complexity of the max heap is Search-Min O(1), Insert O(log(n)), and Delete-Min O(log(n)). The Space complexity of the max heap is O(n). 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 215 | https://leetcode.com/problems/kth-largest-element-in-an-array/ | [this link](../practice/solution/0215_kth_largest_element_in_an_array.py) |
| 218 | https://leetcode.com/problems/the-skyline-problem/ | |
| 347 | https://leetcode.com/problems/top-k-frequent-elements/ | [this link](../practice/solution/0347_top_k_frequent_elements.py) |
| 480 | https://leetcode.com/problems/sliding-window-median/ | |
| 692 | https://leetcode.com/problems/top-k-frequent-words/ | [this link](../practice/solution/0692_top_k_frequent_words.py) |
| 767 | https://leetcode.com/problems/reorganize-string/ | [this link](../practice/solution/0767_reorganize_string.py) |
| 819 | https://leetcode.com/problems/most-common-word/ | [this link](../practice/solution/0819_most_common_word.py) |
| 819* | https://leetcode.com/discuss/interview-question/542597/ | [this link](../practice/a/top_k_frequently_mentioned_keywords.py) |
| 973 | https://leetcode.com/problems/k-closest-points-to-origin/ |[this link](../practice/solution/0973_k_closest_points_to_origin.py) | 
| 1005 | https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/ | |
| 1152 | https://leetcode.com/problems/analyze-user-website-visit-pattern/ | [this link](../practice/solution/1152_analyze_user_website_visit_pattern.py) |