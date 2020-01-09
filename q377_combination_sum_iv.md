# Solutions

* DP Solution
  * Thoughts: 这种DP题都差不多，但是有两个难点
    * 如何分辨该题可以用DP来求解？
      * 看能否分治，即大问题是否能通过小问题来求解，也就是要分辨大问题和小问题之间是否有关系式
    * 如何找到dp数组要存储哪些东西？
      * 看变量，变量变了的话极有可能会有重复计算，要存储的就是子问题的解
      * 看参数，一般参数就有可能是变量
  * Extra: 这个follow up比较有意思，如果有负数的话可能会出现无限循环的组合，比如[-2, 2], target=2，结果可能就是(-2, 2, -2, 2...)
  * Time complexity: $O(n*k)$, n is the target, k is the length of nums
  * Space complexity: $O(n)$