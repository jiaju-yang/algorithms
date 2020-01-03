# Solutions

* Based on Two Sum
  * Thoughts: 这个算法比较容易想到，先排序，然后在迭代的时候把当前的数相当于作为Two Sum里的target，再以Two Sum方式迭代当前数后面的数。缺点是会占用$O(n)$的内存。要注意去重的问题
  * Time complexity: $O(n^2)$
  * Space complexity: $O(n)$
* Two Pointer
  * Thoughts: 先排序，迭代的时候把当前数作为第一个数，设置left=当前数的后一个数，right=数组末尾的数，然后测试current + left + right与0的关系，小于0证明需要变大，就把left往右移，大于0证明需要变小，就把right往左移，等于0证明满足条件，加入result。也要注意去重的问题。比上面的算法好在空间复杂度会降低
  * Time complexity: $O(n^2)$
  * Space complexity: $O(1)$

