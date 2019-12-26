# Solutions

* Brute force
  * Time complexity: $O(n^2)$
  * Space complexity: $O(1)$
* One-pass loop
  * Thoughts: When I loop through each price, I have to loop through the following prices to check if max profit exists. What if I reverse the idea? That is to say, I loop through each sell price instead of buy price. For each sell price, the max profit is the difference between the current sell price and the minimum buy price so far. Therefore, I only have to loop once and record two values: the minimum buy price so far and the maximum profit.
  * Time complexity: $O(n)$
  * Space complexity: $O(1)$