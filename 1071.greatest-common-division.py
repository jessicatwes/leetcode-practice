# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times) Return the largest string X such that X divides str1 and X divides str2.

# Solution - Determine if the two str are made of common divisor. Find the divisor by math.gcd. Return the divisor by using the length of gcd output to split string.

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ''' 
	str1, str2: string inputs
        str1[:gcd_len]: return str of the common divisor  
	'''
	if str1 + str2 != str2 + str1:
            return ""
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]

# Test case str1 = "ABABAB", str2 = "AB"
# gcdOfStrings(str1, str2) #AB 
