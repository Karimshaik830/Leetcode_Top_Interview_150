class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len=0
        left=0
        last={}
        for right,c in enumerate(s):
            if c in last and last[c]>=left:
                left=last[c]+1
            len=max(len,right-left+1)
            last[c]=right
        return len