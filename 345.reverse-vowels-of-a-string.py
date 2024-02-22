# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
	'''
	s: input str
	new_s: return str with vowel reverse
	'''
        vowels = ['a' ,'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            elif s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        new_s = "".join(s)
        return new_s

# Test case s = "hello"
# reverseVowels(s) #"holle"
