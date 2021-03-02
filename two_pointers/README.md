# Two Pointers 

The following questions, I prefer to solve by using Two Pointers. It may have the optimal method, please check the discussion in LeetCode.

* [Array](##Array)
* [String](##String)

## Array

Two pointers are really an easy and effective technique to solve many array related problems in place, especially in technical interviews. The array is one of the fundamental blocks in algorithms. This kind of problem usually involves two pointers: 1) one slow-runner and the other fast-runner, and 2) one pointer starts from the beginning while the other pointer starts from the end.

This type of problem includes: find the 3-4 sum in place problem, remove duplicates element in place problem, sort element in place problem， sliding window implementation (see Special Case)

The time complexity of this technique depends on the question.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 11 | https://leetcode.com/problems/container-with-most-water/ | [this link](../practice/solution/0011_container_with_most_water.py) |
| 15 | https://leetcode.com/problems/3sum/ | [this link](../practice/solution/0015_3sum.py) |
| 16 | https://leetcode.com/problems/3sum-closest/ | [this link](../practice/solution/0016_3sum_closest.py) |
| 18 | https://leetcode.com/problems/4sum/ | [this link](../practice/solution/0018_4sum.py) |
| 26 | https://leetcode.com/problems/remove-duplicates-from-sorted-array/ | [this link](../practice/solution/0026_remove_duplicates_from_sorted_array.py) |
| 27 | https://leetcode.com/problems/remove-element/ | [this link](../practice/solution/0027_remove_element.py) |
| 31 | https://leetcode.com/problems/next-permutation/ | [this link](../practice/solution/0031_next_permutation.py) |
| 67 | https://leetcode.com/problems/add-binary/ | [this link](../practice/solution/0067_add_binary.py) |
| 75 | https://leetcode.com/problems/sort-colors/ | [this link](../practice/solution/0075_sort_colors.py) |
| 88 | https://leetcode.com/problems/merge-sorted-array/ | [this link](../practice/solution/0088_merge_sorted_array.py) |
| 283 | https://leetcode.com/problems/move-zeroes/ | [this link](../practice/solution/0283_move_zeroes.py) |
| 344 | https://leetcode.com/problems/reverse-string/ | [this link](../practice/solution/0344_reverse_string.py) |
| 415 | https://leetcode.com/problems/add-strings/ | [this link](../practice/solution/0415_add_strings.py) |
| 556 | https://leetcode.com/problems/next-greater-element-iii/ | [this link](../practice/solution/0556_next_greater_element_iii.py) |
| 611 | https://leetcode.com/problems/valid-triangle-number/ | [this link](../practice/solution/0611_valid_triangle_number.py) |
| 881 | https://leetcode.com/problems/boats-to-save-people/ | |
| 986 | https://leetcode.com/problems/interval-list-intersections/ | [this link](../practice/solution/0986_interval_list_intersections.py) |
| 1099 | https://leetcode.com/problems/two-sum-less-than-k/ | [this link](../practice/solution/1099_two_sum_less_than_k.py) |
| 1099* | https://leetcode.com/discuss/interview-question/373202 | [this link](../practice/a/optimal_utilization.py) |
| 1229 | https://leetcode.com/problems/meeting-scheduler/ | [this link](../practice/solution/1229_meeting_scheduler.py) |

## String

Since a string is just formed by an array of characters, they are both similar.

This type of problem includes: find partition in target string problem

The time complexity of this technique depends on the question.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 556 | https://leetcode.com/problems/next-greater-element-iii/ | |
| 696 | https://leetcode.com/problems/count-binary-substrings/ | [this link](../practice/solution/0696_count_binary_substrings.py) |
| 763 | https://leetcode.com/problems/partition-labels/ | [this link](../practice/solution/0763_partition_labels.py) |