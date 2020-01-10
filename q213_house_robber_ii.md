# Solutions

* DP Solution
  * Thoughts: 这道题是第198题的扩展，把直线排列的房子变成了圆圈排列。这道题的解题思路是典型的把一个难题变成两个简单点的题，要学会“分”。这道题有一点很奇怪，数组分片按理说会生成新数组，应该会消耗额外的时间，但是运算时间居然还小了一些，猜测可能是`range`的运算速度比较慢。
  * Time complexity: $O(n)$
  * Space complexity: $O(1)$