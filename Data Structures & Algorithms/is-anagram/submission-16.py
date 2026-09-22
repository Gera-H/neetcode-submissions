class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDic = {}
        tDic = {}

        for c in s:
            sDic[c] = 1 + sDic.get(c,0)
        for c in t:
            tDic[c] = 1 + tDic.get(c,0)

        return sDic == tDic
        