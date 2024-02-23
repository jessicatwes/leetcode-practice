# https://leetcode.com/problems/is-subsequence/
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
# Solution - Set counter for each str to track position. Find position in str s that match str t. Keep track of position to keep it subsequential. If i is the length of str s, then we found all the char in str t.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

# Test case s = "abc", t = "ahbgdc"
# isSubsequence(s, t) #True
