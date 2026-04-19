class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        lastFound = {}
        l = 0
        for r in range(len(s)):
            if s[r] in lastFound:
                l = max(lastFound[s[r]]+1,l)
            lastFound[s[r]]=r
            maxl = max(maxl, r-l+1)
            r+=1
        return maxl
        
        