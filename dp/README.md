# Dynamic Programming

The following questions, I prefer to solve by using DP. It may have the optimal method, please check the discussion in LeetCode. When you try to come up a DP solution, you need to know 4 things: 1)state, 2)function, 3)initialization, 4)answer

* [Coordinate DP](##Coordinate-DP) 
* [Sequential DP](##Sequential-DP)
* [Bidirectional Sequence DP](##Bidirectional-Sequence-DP)
* [Interval DP](##Interval-DP)
* [Divided DP](##Divided-DP)
* [Knapsack DP](##Knapsack-DP)
* [Comprehensive DP](##Comprehensive-DP)
* [Game type DP](##Game-type-DP)

## Coordinate DP

This type of problem includes: find status in the checkerboard problem

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 62 | https://leetcode.com/problems/unique-paths/ | [this link](../practice/solution/0062_unique_paths.py)|
| 64 | https://leetcode.com/problems/minimum-path-sum/ | |
| 64* | https://www.1point3acres.com/bbs/thread-595086-1-1.html | |
| 120 | https://leetcode.com/problems/triangle/ | |
| 688 | https://leetcode.com/problems/knight-probability-in-chessboard/| |

## Sequential DP

This type of problem includes: find the longest/shortest common sequence problem, find the longest/shortest increase/decreasing sequence problem, find egg drop problem

For this kind of question, you need to use 1D DP array to transfer state when dealing with comparison

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 53 | https://leetcode.com/problems/maximum-subarray/ | [this link](../practice/solution/0053_maximum_subarray.py) |
| 32 | https://leetcode.com/problems/longest-valid-parentheses/ | [this link](../practice/solution/0032_longest_valid_parentheses.py) |
| 91 | https://leetcode.com/problems/decode-ways/ | [this link](../practice/solution/0091_decode_ways.py) |
| 121 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ | [this link](../practice/solution/0121_best_time_to_buy_and_sell_stock.py) |
| 123 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/ | |
| 135 | https://leetcode.com/problems/candy/ | |
| 309 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ | |
| 821 | https://leetcode.com/problems/shortest-distance-to-a-character/ | |
| 978 | https://leetcode.com/problems/longest-turbulent-subarray/ | |

## Bidirectional Sequence DP

This type of problem includes: find longest/shortest palindromic sequence problem

For this kind of question, you need to use 2D DP array to transfer state when dealing with comparison

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 5 | https://leetcode.com/problems/longest-palindromic-substring/ | [this link](../practice/solution/0005_longest_palindromic_substring.py) |
| 10 | https://leetcode.com/problems/regular-expression-matching/ | [this link](../practice/solution/0010_regular_expression_matching.py) |
| 44 | https://leetcode.com/problems/wildcard-matching/ | [this link](../practice/solution/0044_wildcard_matching.py) |
| 72 | https://leetcode.com/problems/edit-distance/ | [this link](../practice/solution/0072_edit_distance.py) |
| 97 | https://leetcode.com/problems/interleaving-string/ | |
| 887 | https://leetcode.com/problems/super-egg-drop/ | |
| 1035 | https://leetcode.com/problems/uncrossed-lines/ | |
| 1143 | https://leetcode.com/problems/longest-common-subsequence/ | [this link](../practice/solution/1143_longest_common_subsequence.py) |

## Interval DP

This type of problem includes: find the subset problem，find word break problem

For this kind of question, you need to enumerate the left and right subranges and record the state into into 1D or 2D DP array.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 139 | https://leetcode.com/problems/word-break/ | [this link](../practice/solution/0139_word_break.py) |
| 140 | https://leetcode.com/problems/word-break-ii/ | [this link](../practice/solution/0140_word_break_ii.py) |
| 368 | https://leetcode.com/problems/largest-divisible-subset/ | |

## Divided DP

This type of problem includes: find the area sum problem

For this kind of question, you need to preprocess calculate the sum into 1D or 2D DP array.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 221 | https://leetcode.com/problems/maximal-square/ | [this link](../practice/solution/0221_maximal_square.py) |
| 304 | https://leetcode.com/problems/range-sum-query-2d-immutable/ |

## Knapsack DP

This type of problem includes: find 0-1 knapsack problem, find unbound knapsack problem, find bounded knapsack problem, find multi-objective knapsack problem, find multi-dimensional knapsack problem, find multiple knapsack problem, find quadratic knapsack problem

For this kind of quesiton, you need to know what is knapsack problem: a problem in combinatorial optimization: given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 198 | https://leetcode.com/problems/house-robber/ | [this link](../practice/solution/0198_house_robber.py) |
| 256 | https://leetcode.com/problems/paint-house/ | [this link](../practice/solution/0256_paint_house.py) |
| 279 | https://leetcode.com/problems/perfect-squares/ | [this link](../practice/solution/0279_perfect_squares.py) |
| 322 | https://leetcode.com/problems/coin-change/ | [this link](../practice/solution/0322_coin_change.py) |
| 474 | https://leetcode.com/problems/ones-and-zeroes/ | |
| 518 | https://leetcode.com/problems/coin-change-2/ | [this link](../practice/solution/0518_coin_change_2.py) |
| 1049 | https://leetcode.com/problems/last-stone-weight-ii/ | [this link](../practice/solution/1049_last_stone_weight_ii.py) |
| 1155 | https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/ | [this link](../practice/solution/1155_number_of_dice_rolls_with_target_sum.py) |
| 1262 | https://leetcode.com/problems/greatest-sum-divisible-by-three/ | [this link](../practice/solution/1262_greatest_sum_divisible_by_three.py) |
| 1235 | https://leetcode.com/problems/maximum-profit-in-job-scheduling/ | [this link](../practice/solution/1235_maximum_profit_in_job_scheduling.py) |

## Comprehensive DP

This type of problem includes: find the matrix multiplication problem, find the fibonacci sequence problem, find the catalan number problem

For this kind of question, you need to famillar with basic math knowlegae.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 43 | https://leetcode.com/problems/multiply-strings/ | [this link](../practice/solution/0043_multiply_strings.py) |
| 70 | https://leetcode.com/problems/climbing-stairs/ | [this link](../practice/solution/0070_climbing_stairs.py) |
| 96 | https://leetcode.com/problems/unique-binary-search-trees/ | [this link](../practice/solution/0096_unique_binary_search_trees.py) |
| 119 | https://leetcode.com/problems/pascals-triangle-ii/ | [this link](../practice/solution/0119_pascals_triangle_ii.py) |
| 204 | https://leetcode.com/problems/count-primes/ | [this link](../practice/solution/0204_count_primes.py) | 
| 264 | https://leetcode.com/problems/ugly-number-ii/ | [this link](../practice/solution/0264_ugly_number_ii.py) |
| 311 | https://leetcode.com/problems/sparse-matrix-multiplication/ | |
| 509 | https://leetcode.com/problems/fibonacci-number/ | [this link](../practice/solution/0509_fibonacci_number.py) |

## Game-type DP

This type of problem includes: life game-type problem, math game-type problem, policy game-type problem, others game-type problem

For this kind of question, there is a common point that the problem is talking about the comparison or execution sequence.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 152 | https://leetcode.com/problems/maximum-product-subarray/ | [this link](../practice/solution/0152_maximum_product_subarray.py) |
| 486 | https://leetcode.com/problems/predict-the-winner/ | |
| 801 | https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/ | [this link](../practice/solution/0801_minimum_swaps_to_make_sequences_increasing.py) |
| 1048 | https://leetcode.com/problems/longest-string-chain/ | |
| 1153 | https://leetcode.com/problems/string-transforms-into-another-string/ | |
