# Hash Map&Set

The following questions, I prefer to solve by using Heap Map&Set. It may have the optimal method, please check the discussion in LeetCode.  

* [Hash Map](##Hash-Map)
* [Hash Set](##Hash-Set)

## Hash Map

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash map uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions are typically accommodated in some way. In many situations, hash map turn out to be on average more efficient than search trees or any other table lookup structure. For this reason, they are widely used in many kinds of computer software, particularly for associative arrays, database indexing, caches, and sets. [Wikipedia](https://en.wikipedia.org/wiki/Hash_table)

This type of problem includes: create a lookup table for the key-pair problem, create a lookup table for counting duplicate elements problem, two sum implementation (see Special Case)

The time complexity of the hash map is O(1) (Search O(1), Insert O(1), Delete O(1)), and the Space complexity of the hash map is O(n). 

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 13 | https://leetcode.com/problems/roman-to-integer/ | [this link](../practice/solution/0013_roman_to_integer.py) |
| 49 | https://leetcode.com/problems/group-anagrams/ | [this link](../practice/solution/0049_group_anagrams.py) |
| 166 | https://leetcode.com/problems/fraction-to-recurring-decimal/ | [this link](../practice/solution/0166_fraction_to_recurring_decimal.py) |
| 187 | https://leetcode.com/problems/repeated-dna-sequences/ | |
| 219 | https://leetcode.com/problems/contains-duplicate-ii/ | |
| 220 | https://leetcode.com/problems/contains-duplicate-iii/ | |
| 299 | https://leetcode.com/problems/bulls-and-cows/ | [this link](../practice/solution/0299_bulls_and_cows.py) |
| 311 | https://leetcode.com/problems/sparse-matrix-multiplication/ | [this link](../practice/solution/0311_sparse_matrix_multiplication.py) |
| 349 | https://leetcode.com/problems/intersection-of-two-arrays/ | [this link](../practice/solution/0349_intersection_of_two_arrays.py) |
| 350 | https://leetcode.com/problems/intersection-of-two-arrays-ii/ | [this link](../practice/solution/0350_intersection_of_two_arrays_ii.py) |  
| 336 | https://leetcode.com/problems/palindrome-pairs/ | [this link](../practice/solution/0336_palindrome_pairs.py) |
| 387 | https://leetcode.com/problems/first-unique-character-in-a-string/ | [this link](../practice/solution/0387_first_unique_character_in_a_string.py) |
| 438 | https://leetcode.com/problems/find-all-anagrams-in-a-string/ | [this link](../practice/solution/0438_find_all_anagrams_in_a_string.py) |
| 451 | https://leetcode.com/problems/sort-characters-by-frequency/ | |
| 532 | https://leetcode.com/problems/k-diff-pairs-in-an-array/ | [this link](../practice/solution/0532_k_diff_pairs_in_an_array.py) |
| 554 | https://leetcode.com/problems/brick-wall/ | [this link](../practice/solution/0554_brick_wall.py) |
| 560 | https://leetcode.com/problems/subarray-sum-equals-k/ | [this link](../practice/solution/0560_subarray_sum_equals_k.py) |
| 567 | https://leetcode.com/problems/permutation-in-string/ | [this link](../practice/solution/0567_permutation_in_string.py) |
| 599 | https://leetcode.com/problems/minimum-index-sum-of-two-lists/ | [this link](../practice/solution/0599_minimum_index_sum_of_two_lists.py) |
| 609 | https://leetcode.com/problems/find-duplicate-file-in-system/ | [this link](../practice/solution/0609_find_duplicate_file_in_system.py) |
| 621 | https://leetcode.com/problems/task-scheduler/ | [this link](../practice/solution/0621_task_scheduler.py) | 
| 697 | https://leetcode.com/problems/degree-of-an-array/ | |
| 846 | https://leetcode.com/problems/hand-of-straights/ | [this link](../practice/solution/0846_hand_of_straights.py) |
| 953 | https://leetcode.com/problems/verifying-an-alien-dictionary/ | |
| 963 | https://leetcode.com/problems/minimum-area-rectangle-ii/ | |
| 974 | https://leetcode.com/problems/subarray-sums-divisible-by-k/ | [this link](../practice/solution/0974_subarray_sums_divisible_by_k.py) |
| 1138 | https://leetcode.com/problems/alphabet-board-path/ | |
| 1207 | https://leetcode.com/problems/unique-number-of-occurrences/ | |
| 1296 | https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/ | [this link](../practice/solution/1296_divide_array_in_sets_of_k_consecutive_numbers.py) |
| 1410 | https://leetcode.com/problems/html-entity-parser/ | [this link](../practice/solution/1410_html_entity_parser.py) |
| 1153 | https://leetcode.com/problems/string-transforms-into-another-string/ | [this link](../practice/solution/1153_string_transforms_into_another_string.py) |
| | https://leetcode.com/discuss/interview-question/373006 | [this link](../practice/a/favorite_genres.py) |
| | https://www.1point3acres.com/bbs/thread-580122-1-1.html | [this link](../practice/a/user_based_recommendation_system.py) |
| | https://www.1point3acres.com/bbs/thread-610975-1-1.html | [this link](../practice/others/throttling_gateway.py) |

## Hash Set

In computer science, a set is an abstract data type that can store unique values, without any particular order. It is a computer implementation of the mathematical concept of a finite set. Unlike most other collection types, rather than retrieving a specific element from a set, one typically tests a value for membership in a set. [Wikipedia](https://en.wikipedia.org/wiki/Set_(abstract_data_type))

A hash map is an implementation of Map. A Map maps keys to values. The key lookup occurs using the hash. On the other hand, a hash set is an implementation of Set. A Set is designed to match the mathematical model of a set. A hash set does use a HashMap to back its implementation. The hash set does not allow duplicate elements that mean you can not store duplicate values in the hash set. Hash set is quite useful when need verify some information is exists or been used, which can help reduce time complexity by checking in the hash set. 

This type of problem includes: create a lookup table for checking duplicate elements problem

Same as a hash map, the time complexity of the hash set is O(1) (Search O(1), Insert O(1), Delete O(1)), the Space complexity of the hash set is O(n).

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 36 | https://leetcode.com/problems/valid-sudoku/ | [this link](../practice/solution/0036_valid_sudoku.py) |
| 73 | https://leetcode.com/problems/set-matrix-zeroes/ | [this link](../practice/solution/0073_set_matrix_zeroes.py) |
| 128 | https://leetcode.com/problems/longest-consecutive-sequence/ | [this link](../practice/solution/0128_longest_consecutive_sequence.py) |
| 136 | https://leetcode.com/problems/single-number/ | [this link](../practice/solution/0136_single_number.py) | 
| 202 | https://leetcode.com/problems/happy-number/ | [this link](../practice/solution/0202_happy_number.py) |
| 205 | https://leetcode.com/problems/isomorphic-strings/ | [this link](../practice/solution/0205_isomorphic_strings.py) | 
| 217 | https://leetcode.com/problems/contains-duplicate/ |[this link](../practice/solution/0217_contains_duplicate.py) |
| 564 | https://leetcode.com/problems/find-the-closest-palindrome/ | |
| 723 | https://leetcode.com/problems/candy-crush/ | |
| 734 | https://leetcode.com/problems/sentence-similarity/ | |
| 794 | https://leetcode.com/problems/valid-tic-tac-toe-state/ | [this link](../practice/solution/0794_valid_tic_tac_toe_state.py) |
| 929 | https://leetcode.com/problems/unique-email-addresses/ | |
| 970 | https://leetcode.com/problems/powerful-integers/ | |
| 1044 | https://leetcode.com/problems/longest-duplicate-substring/ | |
| 1275 |https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/ | |
| 1380 | https://leetcode.com/problems/lucky-numbers-in-a-matrix/ | [this link](../practice/solution/1380_lucky_numbers_in_a_matrix.py) |
