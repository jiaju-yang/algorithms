# Solutions

* Left and Right Product Lists

  * Thoughts: The most important thing is to visualize how the different products except self look like for each of the elements. Here is an example from [sachimalhotra1993](https://leetcode.com/sachinmalhotra1993)'s [solution](https://leetcode.com/problems/product-of-array-except-self/solution/) in leetcode:

    ![img](q238_product_of_array_except_self.assets/diag-1.png)

    For every given index, we can get the result by multipling the product of all the numbers to the left of the index by the product of all the numbers to the right.

  * Time complexity: $O(n)$

  * Space complexity: $O(n)$

* Optimized Left and Right Product Lists

  * Thoughts: Use the left array as the result. The right array can be omitted cause we only need to record the previous product when we loop through each elements again. Therefore, instead of using an array, we just need a number.
  * Time complexity: $O(n)$
  * Space complexity: $O(1)$ (except the result array)