# Solutions

1. Brute force: Loop through each element and find if there is another value that equals to `target - x`
   * Time complexity: $O(n^2)$
   * Space complexity: $O(1)$
* One-pass Hash Table - *Mine*
  * Thoughts: In brute force solution, I have to check if the complement exists in the array when I loop through each element. This checking action needs to loop through each element again. Therefore, I need to optimize this time-consuming action. I need an $O(1)$ time complexity checking operation. Hash table is the best solution. Typical trading space for speed.
  * Time complexity: $O(n)$
  * Space complexity: $O(n)$