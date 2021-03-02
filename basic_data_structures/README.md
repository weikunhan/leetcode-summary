# Basic Data Structures

The data structures you should know before starting coding in LeetCode:

* Array
* Linked List
* Stack
* Queue
* Binary Tree
* Binary Search Tree
* Red-Black Tree
* Heap
* Hash Table
* Graph
* Advanced Data Structure

For more information, you need to check related courses and books. Here, most basic data structures are:

* [Array](##Array)
* [Linked List](##Linked-List)
* [String (Not a data structure)](##String)

## Array

In computer science, an array data structure, or simply an array, is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. An array is stored such that the position of each element can be computed from its index tuple by a mathematical formula. The simplest type of data structure is a linear array, also called one-dimensional array. For example, an array of 10 32-bit (4-byte) integer variables, with indices 0 through 9, may be stored as 10 words at memory addresses 2000, 2004, 2008, ..., 2036, so that the element with index i has the address 2000 + (i × 4). The memory address of the first element of an array is called first address, foundation address, or base address. Because the mathematical concept of a matrix can be represented as a two-dimensional grid, two-dimensional arrays are also sometimes called matrices. In some cases the term "vector" is used in computing to refer to an array, although tuples rather than vectors are the more mathematically correct equivalent. Tables are often implemented in the form of arrays, especially lookup tables; the word table is sometimes used as a synonym of array. Arrays are among the oldest and most important data structures, and are used by almost every program. They are also used to implement many other data structures, such as lists and strings. They effectively exploit the addressing logic of computers. In most modern computers and many external storage devices, the memory is a one-dimensional array of words, whose indices are their addresses. Processors, especially vector processors, are often optimized for array operations. Arrays are useful mostly because the element indices can be computed at run time. Among other things, this feature allows a single iterative statement to process arbitrarily many elements of an array. For that reason, the elements of an array data structure are required to have the same size and should use the same data representation. The set of valid index tuples and the addresses of the elements (and hence the element addressing formula) are usually, but not always,fixed while the array is in use. [Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure)

For programming practice, you need to know how to: 1)iterate through 1D array, 2)iterate through 2D array, 3)play tricks using different programming languages, 4)understand bit manipulation

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 14 | https://leetcode.com/problems/longest-common-prefix/ | [this link](../practice/solution/0014_longest_common_prefix.py) |
| 41 | https://leetcode.com/problems/first-missing-positive/ | [this link](../practice/solution/0041_first_missing_positive.py) |
| 54 | https://leetcode.com/problems/spiral-matrix/ | [this link](../practice/solution/0054_spiral_matrix.py) |
| 56 | https://leetcode.com/problems/merge-intervals/ | [this link](../practice/solution/0056_merge_intervals.py) |
| 57 | https://leetcode.com/problems/insert-interval/ | [this link](../practice/solution/0057_insert_interval.py) |
| 59 | https://leetcode.com/problems/spiral-matrix-ii/ | [this link](../practice/solution/0059_spiral_matrix_ii.py) |
| 66 | https://leetcode.com/problems/plus-one/ | [this link](../practice/solution/0066_plus_one.py) | 
| 167 | https://leetcode.com/problems/majority-element/ | [this link](../practice/solution/0169_majority_element.py) |
| 189 | https://leetcode.com/problems/rotate-array/ | [this link](../practice/solution/0189_rotate_array.py) |
| 238 | https://leetcode.com/problems/product-of-array-except-self/ | [this link](../practice/solution/0238_product_of_array_except_self.py) |
| 243 | https://leetcode.com/problems/shortest-word-distance/ | [this link](../practice/solution/0243_shortest_word_distance.py) |
| 268 | https://leetcode.com/problems/missing-number/ | [this link](../practice/solution/0268_missing_number.py) | 
| 277 | https://leetcode.com/problems/find-the-celebrity/ | [this link](../practice/solution/0277_find_the_celebrity.py) |
| 287 | https://leetcode.com/problems/find-the-duplicate-number/ | [this link](../practice/solution/0287_find_the_duplicate_number.py) |
| 334 | https://leetcode.com/problems/increasing-triplet-subsequence/ | [this link](../practice/solution/0334_increasing_triplet_subsequence.py) |
| 386 | https://leetcode.com/problems/lexicographical-numbers/ | [this link](../practice/solution/0386_lexicographical_numbers.py) | 
| 406 | https://leetcode.com/problems/queue-reconstruction-by-height/ | [this link](../practice/solution/0406_queue_reconstruction_by_height.py) |
| 442 | https://leetcode.com/problems/find-all-duplicates-in-an-array/ | [this link](../practice/solution/0442_find_all_duplicates_in_an_array.py) |
| 605 | https://leetcode.com/problems/can-place-flowers/ | [this link](../practice/solution/0605_can_place_flowers.py) |
| 628 | https://leetcode.com/problems/maximum-product-of-three-numbers/ | [this link](../practice/solution/0628_maximum_product_of_three_numbers.py) |
| 759 | https://leetcode.com/problems/employee-free-time/ | [this link](../practice/solution/0759_employee_free_time.py) |
| 766 | https://leetcode.com/problems/toeplitz-matrix/ | [this link](../practice/solution/0766_toeplitz_matrix.py) |
| 836 | https://leetcode.com/problems/rectangle-overlap/ | [this link](../practice/solution/0836_rectangle_overlap.py) | 
| 945 | https://leetcode.com/problems/minimum-increment-to-make-array-unique/ | [this link](../practice/solution/0945_minimum_increment_to_make_array_unique.py) |
| 957 | https://leetcode.com/problems/prison-cells-after-n-days/ | [this link](../practice/solution/0957_prison_cells_after_n_days.py) |
| 977 | https://leetcode.com/problems/squares-of-a-sorted-array/ | [this link](../practice/solution/0977_squares_of_a_sorted_array.py) |
| 1013 | https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/ | [this link](../practice/solution/1013_partition_array_into_three_parts_with_equal_sum.py) |
| 1031 | https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/ | [this link](../practice/solution/1031_maximum_sum_of_two_non_overlapping_subarrays.py) |
| 1243 | https://leetcode.com/problems/array-transformation/ | [this link](../practice/solution/1243_array_transformation.py) |
| 1356 | https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/ | [this link](../practice/solution/1356_sort_integers_by_the_number_of_1_bits.py) |
| 1428 | https://leetcode.com/problems/leftmost-column-with-at-least-a-one/ | [this link](../practice/solution/1428_leftmost_column_with_at_least_a_one.py) |
| | https://www.1point3acres.com/bbs/thread-642190-1-1.html | [this link](../practice/others/min_cost_to_racing_track_end.py) |
| | https://www.1point3acres.com/bbs/thread-592043-1-1.html | [this link](../practice/others/subsequence_removal.py) |
| | https://www.1point3acres.com/bbs/thread-592043-1-1.html | [this link](../practice/others/subsequence_removal_ii.py) | 
| | https://www.1point3acres.com/bbs/thread-592043-1-1.html | [this link](../practice/others/subsequence_removal_iii.py) |

## Linked List

In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists. Linked lists are among the simplest and most common data structures. They can be used to implement several other common abstract data types, including lists, stacks, queues, associative arrays, and S-expressions, though it is not uncommon to implement those data structures directly without using a linked list as the basis. [Wikipedia](https://en.wikipedia.org/wiki/Linked_list)

This type of problem includes: 1)delete elements in the linked list, 2)insert elements in the linked list. 3)merge elements from two linked lists 4)rotate elements in a linked list, 5)copy special linked list

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 2 | https://leetcode.com/problems/add-two-numbers/ | [this link](../practice/solution/0002_add_two_numbers.py) |
| 19 | https://leetcode.com/problems/remove-nth-node-from-end-of-list/ | [this link](../practice/solution/0019_remove_nth_node_from_end_of_list.py) |
| 21 | https://leetcode.com/problems/merge-two-sorted-lists/ | [this link](../practice/solution/0021_merge_two_sorted_lists.py) |
| 23 | https://leetcode.com/problems/merge-k-sorted-lists/ | [this link](../practice/solution/0023_merge_k_sorted_lists.py) |
| 24 | https://leetcode.com/problems/swap-nodes-in-pairs/ | [this link](../practice/solution/0024_swap_nodes_in_pairs.py) |
| 25 | https://leetcode.com/problems/reverse-nodes-in-k-group/ | [this link](../practice/solution/0025_reverse_nodes_in_k_group.py) |
| 82 | https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ | |
| 83 | https://leetcode.com/problems/remove-duplicates-from-sorted-list/ | [this link](../practice/solution/0083_remove_duplicates_from_sorted_list.py) |
| 86 | https://leetcode.com/problems/partition-list/ | |
| 92 | https://leetcode.com/problems/reverse-linked-list-ii/ | [this link](../practice/solution/0092_reverse_linked_list_ii.py) |
| 138 | https://leetcode.com/problems/copy-list-with-random-pointer/ | [this link](../practice/solution/0138_copy_list_with_random_pointer.py) |
| 141 | https://leetcode.com/problems/linked-list-cycle/ | [this link](../practice/solution/0141_linked_list_cycle.py) |
| 143 | https://leetcode.com/problems/reorder-list/ | [this link](../practice/solution/0143_reorder_list.py) |
| 148 | https://leetcode.com/problems/sort-list/ | [this link](../practice/solution/0148_sort_list.py) |
| 160 | https://leetcode.com/problems/intersection-of-two-linked-lists/ | [this link](../practice/solution/0160_intersection_of_two_linked_lists.py) |
| 203 | https://leetcode.com/problems/remove-linked-list-elements/ | |
| 206 | https://leetcode.com/problems/reverse-linked-list/ | [this link](../practice/solution/0206_reverse_linked_list.py) |
| 234 | https://leetcode.com/problems/palindrome-linked-list/ | [this link](../practice/solution/0234_palindrome_linked_list.py) |
| 237 | https://leetcode.com/problems/delete-node-in-a-linked-list/ | |
| 328 | https://leetcode.com/problems/odd-even-linked-list/ | [this link](../practice/solution/0328_odd_even_linked_list.py) |
| 369 | https://leetcode.com/problems/plus-one-linked-list/ | |
| 445 | https://leetcode.com/problems/add-two-numbers-ii/ | [this link](../practice/solution/0445_add_two_numbers_ii.py) |
| 708 | https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/ | |
| 876 | https://leetcode.com/problems/middle-of-the-linked-list/ | [this link](../practice/solution/0876_middle_of_the_linked_list.py) | 

## String

In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation). A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures. Depending on the programming language and precise data type used, a variable declared to be a string may either cause storage in memory to be statically allocated for a predetermined maximum length or employ dynamic allocation to allow it to hold a variable number of elements. [Wikipedia](https://en.wikipedia.org/wiki/String_(computer_science))

String is not a data structure but many coding problems play with it. Python strings are "immutable" which means they cannot be changed after they are created (Java strings also use this immutable style). Since strings can't be changed, we construct *new* strings as we go to represent computed values. 

This type of problem includes: 1)sort string syntax, 2)split and join string syntax, 3)encoding and decoding string syntax, 4)regular expression, 5)common string methods, 6)Unix utilities(optional)

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 6 | https://leetcode.com/problems/zigzag-conversion/ | [this link](../practice/solution/0006_zigzag_conversion.py) | 
| 8 | https://leetcode.com/problems/string-to-integer-atoi/ | [this link](../practice/solution/0008_string_to_integer_atoi.py) | 
| 12 | https://leetcode.com/problems/integer-to-roman/ | [this link](../practice/solution/0012_integer_to_roman.py)|
| 28 | https://leetcode.com/problems/implement-strstr/ | [this link](../practice/solution/0028_implement_strstr.py) |
| 38 | https://leetcode.com/problems/count-and-say/ | [this link](../practice/solution/0038_count_and_say.py) |
| 58 | https://leetcode.com/problems/length-of-last-word/ | [this link](../practice/solution/0058_length_of_last_word.py) | 
| 65 | https://leetcode.com/problems/valid-number/ | [this link](../practice/solution/0065_valid_number.py) |
| 68 | https://leetcode.com/problems/text-justification/ | [this link](../practice/solution/0068_text_justification.py) |
| 93 | https://leetcode.com/problems/restore-ip-addresses/ | [this link](../practice/solution/0093_restore_ip_addresses.py) |
| 125 | https://leetcode.com/problems/valid-palindrome/ | [this link](../practice/solution/0125_valid_palindrome.py) |
| 151 | https://leetcode.com/problems/reverse-words-in-a-string/ | [this link](../practice/solution/0151_reverse_words_in_a_string.py) |
| 163 | https://leetcode.com/problems/missing-ranges/ | [this link](../practice/solution/0163_missing_ranges.py) |
| 165 | https://leetcode.com/problems/compare-version-numbers/ | [this link](../practice/solution/0165_compare_version_numbers.py) |
| 179 | https://leetcode.com/problems/largest-number/ | [this link](../practice/solution/0179_largest_number.py) |
| 191 | https://leetcode.com/problems/number-of-1-bits/ | [this link](../practice/solution/0191_number_of_1_bits.py) |
| 214 | https://leetcode.com/problems/shortest-palindrome/ | [this link](../practice/solution/0214_shortest_palindrome.py) | 
| 242 | https://leetcode.com/problems/valid-anagram/ | [this link](../practice/solution/0242_valid_anagram.py) |
| 405 | https://leetcode.com/problems/convert-a-number-to-hexadecimal/ | |
| 419 | https://leetcode.com/problems/battleships-in-a-board/ | |
| 468 | https://leetcode.com/problems/validate-ip-address/ | |
| 640 | https://leetcode.com/problems/solve-the-equation/ | |
| 678 | https://leetcode.com/problems/valid-parenthesis-string/ | [this link](../practice/solution/0678_valid_parenthesis_string.py) |
| 680 | https://leetcode.com/problems/valid-palindrome-ii/ | [this link](../practice/solution/0680_valid_palindrome_ii.py) | 
| 681 | https://leetcode.com/problems/next-closest-time/ | [this link](../practice/solution/0681_next_closest_time.py) |
| 722 | https://leetcode.com/problems/remove-comments/ | [this link](../practice/solution/0722_remove_comments.py) |
| 777 | https://leetcode.com/problems/swap-adjacent-in-lr-string/ | [this link](../practice/solution/0777_swap_adjacent_in_lr_string.py) |
| 796 | https://leetcode.com/problems/rotate-string/ | [this link](../practice/solution/0796_rotate_string.py) |
| 806 | https://leetcode.com/problems/number-of-lines-to-write-string/ | |
| 937 | https://leetcode.com/problems/reorder-data-in-log-files/ | [this link](../practice/solution/0937_reorder_data_in_log_files.py) |