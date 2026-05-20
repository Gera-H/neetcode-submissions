class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        n = len(s)
        if n == 1:
            return 1

        for i in range(n):
            setNew = set()
            setNew.add(s[i])
            for j in range(i+1, n):
                if s[j] in setNew:
                    count = len(setNew)
                    result = max(result, count)
                    print(result)
                    break
                else:
                    setNew.add(s[j])
                    count = len(setNew)
                    result = max(result, count)
        return result