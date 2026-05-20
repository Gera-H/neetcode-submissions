class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sub = set()
        count = 0
        l = 0
        p = 0
        for i in range(n):
            while(s[i] in sub):
                sub.remove(s[p])
                p+=1
            sub.add(s[i])
            l = max(l, len(sub))
        return l