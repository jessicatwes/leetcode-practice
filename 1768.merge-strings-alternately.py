# https://leetcode.com/problems/merge-strings-alternately/
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                merge += word1[i] 
            if i < len(word2):
                merge += word2[i]    
        return merge


# Test case: word1 = "abc", word2 = "pqr"
# mergeAlternately(word1, word2) #"apbqcr"
