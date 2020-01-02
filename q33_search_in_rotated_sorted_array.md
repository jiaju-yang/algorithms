# Solutions

* Binary Search
  * Thoughts: If the array is sorted, the first idea comes into my mind should be Binary Search. Be careful about the IndexError. 这道题的思路其实很简单，每一次把中间值和要搜索的数组段的第一个值相比：如果中间值大于第一个值，说明中间值左边一段是按顺序排列的，然后判断目标值是否在这一区间，如果不在就在中间值右边继续搜索；如果中间值不大于第一个值，说明中间值右边是按顺序排列的，然后判断目标值是否在这一区间，如果不在就在中间值左边继续搜索。其实就是先分两类，每一类中再分两类。
  * Time complexity: $O(log(n))$

  * Space complexity: $O(1)$