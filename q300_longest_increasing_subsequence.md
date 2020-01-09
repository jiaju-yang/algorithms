# Solutions

* DP Solution

  * Thoughts: 可以用动态规划来求解：1. 分治：第i个数之前的LIS跟后面的数无关；2. 关系：第i+1个数之前的LIS可以用$max(\\LIS(i)(if\ nums[i+1]>nums[i]),\\LIS(i-1)(if\ nums[i+1]>nums[i-1]),\\...)$ 

    来计算；3. 存储：用一个一维数组来保存第i个数（包括）之前的LIS

  * Time complexity: $O(n^2)$

  * Space complexity: $O(n)$

* DP Solution with Binary Search

  * Thoughts: So awesome! But a little difficult. 主要思想是用二分查找优化查找过程，但是有一些技巧。这次的dp不存之前的LIS了，而是存之前的LIS本身，并且如果第i个数大于LIS的最后一个数，就在数组最后append；如果不大于，就用二分查找找出是在LIS的第j个位置来大于之前的j-1个数，然后把LIS的第j个位置的数替换成数组的第i个数。最后返回的是LIS的长度，很有意思的解法。
  * Time complexity: $O(n\log{n})$
  * Space complexity: $O(n)$