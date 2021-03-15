# Special Case

The following questions, I prefer to solve by some not commonly used methods. If you interest in more about those methods, please find more material about this method.

* [Two Sum](##Two-Sum)
* [Sliding Window](##Sliding-Window)
* [Math](##Math)
* [Prefix Tree](##Prefix-Tree)
* [Greedy](##Greedy)
* [Topological Sort](##Topological-Sort)
* [Binary Indexed Tree](##Binary-Indexed-Tree)

## Two Sum

Two Sum related problems can simply solve using Two Pointers. I would like to make Two Sum problems as a special case because there is a faster algorithm that will find pairs that sum to the target value in linear time. The algorithm is using a hash map to mapping the target value with an index that has a constant lookup time.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 1 | https://leetcode.com/problems/two-sum/ | [this link](../practice/solution/0001_two_sum.py) |
| 1* | https://leetcode.com/discuss/interview-question/356960 | [this link](../practice/a/find_pair_with_given_sum.py) |
| 1* | https://leetcode.com/discuss/interview-question/372434 | [this link](../practice/a/two_sum_unique_pairs.py) |
| 167 | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ | [this link](../practice/solution/0167_two_sum_ii_input_array_is_sorted.py) |
| 454 | https://leetcode.com/problems/4sum-ii/ | [this link](../practice/solution/0454_4sum_ii.py) |

## Sliding Window

The sliding window algorithm can be used to solve the problem of array/string sub-elements. It can convert the nested loop problem into a single loop problem and reduce the time complexity. For the template for this kind of problem, you need a hash map or hash set and Two Pointers.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 3 | https://leetcode.com/problems/longest-substring-without-repeating-characters/ | [this link](../practice/solution/0003_longest_substring_without_repeating_characters.py) |
| 30 | https://leetcode.com/problems/substring-with-concatenation-of-all-words/ | |
| 76 | https://leetcode.com/problems/minimum-window-substring/ | [this link](../practice/solution/0076_minimum_window_substring.py) |
| 209 | https://leetcode.com/problems/minimum-size-subarray-sum/ | [this link](../practice/solution/0209_minimum_size_subarray_sum.py) |
| 340 | https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/ | [this link](../practice/solution/0340_longest_substring_with_at_most_k_distinct_characters.py) |
| 992 | https://leetcode.com/problems/subarrays-with-k-different-integers/ | [this link](../practice/solution/0992_subarrays_with_k_different_integers.py) |
| 992* | https://leetcode.com/discuss/interview-question/370157 | [this link](../practice/a/substrings_with_exactly_k_distinct_chars.py) |
| 992* | https://leetcode.com/discuss/interview-question/370112 | [this link](../practice/a/substrings_of_size_k_with_k_distinct_chars.py) |
| 995 | https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/ | |
| 1004 | https://leetcode.com/problems/max-consecutive-ones-iii/ | [this link](../practice/solution/1004_max_consecutive_ones_iii.py) |
| 1100 | https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/ | |
| 1052 | https://leetcode.com/problems/grumpy-bookstore-owner/ | |

## Math

There are few problems that are related to mathematical. You should familiar with common methods to play mathematical in computer science. For example, to identify whether a natural number is a prime number, just look at whether it is from 2 to the root N whether it can be divided by N.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 7 | https://leetcode.com/problems/reverse-integer/ | [this link](../practice/solution/0007_reverse_integer.py) |
| 9 | https://leetcode.com/problems/palindrome-number/ | [this link](../practice/solution/0009_palindrome_number.py) |
| 50 | https://leetcode.com/problems/powx-n/ | [this link](../practice/solution/0050_powx_n.py) | 
| 69 | https://leetcode.com/problems/sqrtx/ | |
| 289 | https://leetcode.com/problems/game-of-life/ | [this link](../practice/solution/0289_game_of_life.py) |
| 365 | https://leetcode.com/problems/water-and-jug-problem/ | |
| 367 | https://leetcode.com/problems/valid-perfect-square/ | |
| 412 | https://leetcode.com/problems/fizz-buzz/ | [this link](../practice/solution/0412_fizz_buzz.py) |
| 440 | https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/ | [this link](../practice/solution/0440_k_th_smallest_in_lexicographical_order.py) | 
| 461 | https://leetcode.com/problems/hamming-distance/ | |
| 477 | https://leetcode.com/problems/total-hamming-distance/ | |
| 492 | https://leetcode.com/problems/construct-the-rectangle/ | |
| 633 | https://leetcode.com/problems/sum-of-square-numbers/ | |
| 650 | https://leetcode.com/problems/2-keys-keyboard/ | |
| 780 | https://leetcode.com/problems/reaching-points/ | |
| 866 | https://leetcode.com/problems/prime-palindrome/ | |
| 905 | https://leetcode.com/problems/sort-array-by-parity/ | [this link](../practice/solution/0905_sort_array_by_parity.py) | 
| 991 | https://leetcode.com/problems/broken-calculator/ | |
| 1131 | https://leetcode.com/problems/maximum-of-absolute-value-expression/ | |
| 1175 | https://leetcode.com/problems/prime-arrangements/ | |
| 1185 | https://leetcode.com/problems/day-of-the-week/ | |
| 1344 | https://leetcode.com/problems/angle-between-hands-of-a-clock/ | |
| 1360 | https://leetcode.com/problems/number-of-days-between-two-dates/ | |

## Prefix Tree

In computer science, a trie, also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings. Unlike a binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated; i.e., the value of the key is distributed across the structure. All the descendants of a node have a common prefix of the string associated with that node, and the root is associated with the empty string. Keys tend to be associated with leaves, though some inner nodes may correspond to keys of interest. Hence, keys are not necessarily associated with every node. For the space-optimized presentation of prefix tree, see compact prefix tree. [Wikipedia](https://en.wikipedia.org/wiki/Trie)

To solve this kind of problem, you need to build a trie. The core content to build trie: 1) insert function, 2) search function. Please prepare the template for this kind of problem. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 212 | https://leetcode.com/problems/word-search-ii/ | [this link](../practice/solution/0212_word_search_ii.py) |
| 425 | https://leetcode.com/problems/word-squares/ | [this link](../practice/solution/0425_word_squares.py) |
| 720 | https://leetcode.com/problems/longest-word-in-dictionary/ | |
| 1268 | https://leetcode.com/problems/search-suggestions-system/ | [this link](../practice/solution/1268_search_suggestions_system.py)| 

## Greedy

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time. [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)

To solve this kind of problem, you could reference example like the travelling salesman problem.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 41 | https://leetcode.com/problems/first-missing-positive/ | |
| 45 | https://leetcode.com/problems/jump-game-ii/ | [this link](../practice/solution/0045_jump_game_ii.py) |
| 55 | https://leetcode.com/problems/jump-game/ | [this link](../practice/solution/0055_jump_game.py) |
| 122 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ | [this link](../practice/solution/0122_best_time_to_buy_and_sell_stock_ii.py) |
| 252 | https://leetcode.com/problems/meeting-rooms/ | [this link](../practice/solution/0252_meeting_rooms.py) |
| 253 | https://leetcode.com/problems/meeting-rooms-ii/ | [this link](../practice/solution/0253_meeting_rooms_ii.py) |
| 321 | https://leetcode.com/problems/create-maximum-number/ | |
| 435 | https://leetcode.com/problems/non-overlapping-intervals/ | [this link](../practice/solution/0435_non_overlapping_intervals.py) | 
| 759 | https://leetcode.com/problems/employee-free-time/ | |
| 860 | https://leetcode.com/problems/lemonade-change/ | |
| 1029 | https://leetcode.com/problems/two-city-scheduling/ | |

## Topological Sort

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks. A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG). [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)

To solve this kind of problem, you need two steps: 1)initial graph, 2)use BFS to prune graph.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 207 | https://leetcode.com/problems/course-schedule/ | [this link](../practice/solution/0207_course_schedule.py) |
| 210 | https://leetcode.com/problems/course-schedule-ii/ | [this link](../practice/solution/0210_course_schedule_ii.py)|
| 269 | https://leetcode.com/problems/alien-dictionary/ | [this link](../practice/solution/0269_alien_dictionary.py) |
| 310 | https://leetcode.com/problems/minimum-height-trees/ | |

## Binary Indexed Tree

A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers. This structure was proposed by Boris Ryabko in 1989 with a further modification published in 1992. It has subsequently become known under the name Fenwick tree after Peter Fenwick who described this structure in his 1994 paper. When compared with a flat array of numbers, the Fenwick tree achieves a much better balance between two operations: element update and prefix sum calculation. In a flat array of n numbers, you can either store the elements, or the prefix sums. In the first case, computing prefix sums requires linear time; in the second case, updating the array elements requires linear time (in both cases, the other operation can be performed in constant time). Fenwick trees allow both operations to be performed in O(log n) time. [Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)

From my understanding, the binary indexed tree is another evolution from divided DP. However, when you want to change the preprocessing sum in divided DP, it takes O(n) time, which is not efficient in some cases. Then you may need to choose the binary indexed tree. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 315 | https://leetcode.com/problems/count-of-smaller-numbers-after-self/ | [this link](../practice/solution/0315_count_of_smaller_numbers_after_self.py) |
| 493 | https://leetcode.com/problems/reverse-pairs/ | [this link](../practice/solution/0493_reverse_pairs.py) |