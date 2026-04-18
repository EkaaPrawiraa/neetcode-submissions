class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = 0
        start = 0
        for i,c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            seen[c]=i
            length = max(length,i-start+1)
        return length

        