# Solutions

* Optimized DP Solution
  * Thoughts: 这道题的优化过程还是比较有意思，先想到了DP，但是时间复杂度为$O(n^2)$，导致时间超时；然后想到可以用一个数组来记录可以到达`last_index`的`index`，只在这个数组中遍历就可以了；然后又想到其实用不着记录所有的可以到达`last_index`的`index`，只用记录最近的一个`index`就可以，所以最后直接可以优化成$O(n)$复杂度的算法
  * Time complexity: $O(n)$
  * Space complexity: $O(1)$