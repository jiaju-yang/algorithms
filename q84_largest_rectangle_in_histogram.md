# Solutions

* Stack Solution

  * Thoughts: Genius! Hard to understand. 基本思想和Brute Force Solution一样，还是为了找到每个bar高度的最大面积，要分别从左右找到边界。首先给一个栈，栈里面存储的是`i`，从左往右迭代，如果高度在上升，那么就说明迭代的这些bar都只有左边界而没有右边界，于是把它们的`i`全部存起来留待之后找到右边界后再计算面积，当高度开始下降时，说明有一些之前存起来的bar有右边界了，就要开始计算这部分bar的面积了。假如此时迭代到第`i`个bar，第`i-1`个bar的高度大于第`i`个bar，那么第`i`个bar就是之前的所有高度大于第`i`个bar高度的bar的右边界（注意，第`i`个bar是没有被包含进这个面积的），而它们的左边界就是栈中的第二个bar的右边一位的位置（注意，栈中的第二个bar的位置是没有被包含进这个面积的），高度是取出来的bar的高度。这真的是一个天才般的想法！栈的运用巧妙至极，边界的设定也非常巧妙！
  * Time complexity: $O(n)$

  * Space complexity: $O(n)$, only when the worst situation(always increasing heights)

* DP Solution

  * Thoughts: 这个解法是在Brute Force Solution上优化而来。对于Brute Force Solution中的第二个循环，重复迭代了很多次，所以可以采用dp的方式把这个前后的不低于`heights[i]`的位置记下来。具体来说先用一个迭代从左到右遍历计算`i`的左边的宽度位置，对于第`i`个位置来说，它左边`i-1`的高度如果是大于它自己`i`的高度，那么`dp[i-1]`的位置所记的左边宽度对于`i`位置也是有效的，假设这个位置是`i-3`，如果`i-3`的位置的高度仍然大于`i`的位置的高度，那么继续迭代，直到找到一个位置的高度小于位置`i`的高度；计算右边宽度位置就从右到左遍历。省下的就和Brute Force Solution一样了。
  * Time complexity: $O(n)$，前面两个找寻宽度的循环中又嵌套了一个循环，不过这个循环平均来说只会有$O(1)$次操作

  * Space complexity: $O(n)$, always

* Brute Force Solution

  * Thoughts: 暴力解法也有好几种，有些很难优化，有些可以优化，采取的是可以优化的一种。对于每一根bar `i`来说，它所在的长方形的最大面积高不会低于它自己的高度，而宽是在它的前后，所以就要在它的前后寻找高不低于`height[i]`的bar。可以想象一下下面这个图表，这就是当迭代到第`i=2`位置时找寻到的左边的边界就是`i`本身，右边是第`i=3`位置的bar

    ![img](q84_largest_rectangle_in_histogram.assets/leetcode-q84-2.png)

  * Time complexity: $O(n^2)$

  * Space complexity: $O(1)$