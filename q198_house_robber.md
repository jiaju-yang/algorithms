# Solutions

* DP Solution
  * Thoughts: 这道题很有意思，我发现我的思维和solution的思维不一样。但这两个思维本质上是相同的，因为其实我的思维中的`i-3`的钱已经包含在别人思维中的`i-2`中了，这也是为什么别人的思维下只用记住两个数字
    * 我：当前能抢的钱来自于i-2或i-3抢的最多的钱加上当前房子的钱，所以，需要记住的实际上是三个数字`i-1`, `i-2`, `i-3`
    * 别人：对当前房子只有两个两个动作：抢和不抢。因此，到当前房子为止，抢得最多的来自于（i-2和当前房子的钱）或i-1的钱，所以，需要记住的实际上是两个数字`i-1`, `i-2`
  * extra: [A great explanation](https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.) about DP
  * Time complexity: $O(n)$
  * Space complexity: $O(1)$