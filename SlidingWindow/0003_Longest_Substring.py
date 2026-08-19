from tabulate import PRESERVE_WHITESPACE


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charakters=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in charakters:
                charakters.remove(s[left])
                left+=1
            charakters.add(s[right])
            max_len=max(max_len,right-left+1)

        return max_len


