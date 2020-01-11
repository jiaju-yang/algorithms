# Solutions

* DP Solution
  * Thoughts: 这个方法没实现代码。也是从Brute Force Solution中想出来的，也是为了优化第二个找寻左右最高值的循环，因为这个循环实际上是重复计算了很多次，所以提前用两个循环把每个位置的左右最高值都先存到两个数组中，迭代的时候就直接从这两个数组中拿取该位置的左右最高值。
  * Time complexity: $O(n)$
  * Space complexity: $O(n)$

* Stack Solution
  * Thoughts: 这个方法很不容易理解。从height左边开始迭代，当`height`下降时把`i`存进栈中，当`height`上升时就把栈里的高度一个个拿出来收集水，每次其实收集的是一横排的水，而不是`height[i]`的水。可以这么想象：一个山谷中的水，每一排一排地被收集掉。
  * Time complexity: $O(n)$
  * Space complexity: $O(n)$, stairs-like or flat structure
* Optimized Two Pointer Solution
  * Thoughts: 这个方法也不太容易理解。不找最高height，记录`left_max`和`right_max`，直接左右两个指针开始迭代，当`left`指针迭代到位置`left`时，这时如果左右`left_max`和`right_max`都比`left`大，无论中间的高度怎样变，`left`位置的水都是可以被收集的，而它收集的数量取决于最短的那个`max`，所以把该位置的水收集后下次迭代移动`max`值小的那边的指针，直到两个指针相遇。相比Two Pointer Solution，因为收集的水是取决于小的那根的高度，所以根本用不着最高height，比如收集`left`位置水时，其实取决于`left_max`，因为右边无论是`max_height`还是`right_max`都比`left_max`大，而两个方法中该位置的`left_max`都是不变的
  * Time complexity: $O(n)$，theoretically faster than Two Pointer Solution since doesn't need to find `max_height`, which is at least $O(n)$, but actually 56ms(Optimized Two Pointer Solution) > 52ms(Two Pointer Solution). Weird. Maybe the lengths of height array in tests are not enough.
  * Space complexity: $O(1)$

* Two Pointer Solution
  * Thoughts: 这个双指针解法是在Brute Force Solution的基础上想到的，既然每次迭代i高度的时候都要找到左边和右边的最高值，能否一开始就找到这两个值，当i递增时，左边的最高值很好优化，可以直接记录，但右边不好优化。所以想到了先找到height的最高值位置，用这个位置把height数组分为两半，分别从左右两边往最高值迭代：从左边往右边迭代时，用一个值记录左边的最高值，右边的最高值就是之前找到的整个height的最高值；右边反之。剩余就和Brute Force Solution一样了。
  * Time complexity: $O(n)$
  * Space complexity: $O(1)$

* Brute Force Solution
  * Thoughts: 暴力解法的思想很简单，就是迭代所有高度，在第i个高度的时候分别迭代i左边和右边的所有高度，找到左边和右边的最高值，然后用这两个值的最低值与i的height相比，如果这个值比i的height值大，就证明这个i点可以存储`min(max_left, max_right)-height[i]`的水
  * Time complexity: $O(n^2)$
  * Space complexity: $O(1)$

