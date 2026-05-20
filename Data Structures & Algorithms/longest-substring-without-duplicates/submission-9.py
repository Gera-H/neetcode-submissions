class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sub = set()
        count = 0
        l = 0
        p = 0
        for i in range(n):
            if s[i] in sub:
                count = len(sub)
                l = max(count, l)
                while(s[i] in sub):
                    sub.remove(s[p])
                    p+=1
                sub.add(s[i])

            else:
                sub.add(s[i])
                count = len(sub)
                l = max(count, l)
        return l