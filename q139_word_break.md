# Solutions

* DP Solution
  * Thoughts: 迭代整个字符串，看第i个字符（包括）之前的几个字符合在一起是否在单词表中，如果在，并且排除掉这个字符的前`i-word_length`个字符之前的字符串也能被分割，就证明这个位置之前的字符串都能被分割
  * Time complexity: $O(nk)$, k is the max length of all the given word

  * Space complexity: $O(n)$