class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashAnagram = defaultdict(list)
        result = []
        for s in strs:
            st = tuple(sorted(s))
            hashAnagram[st].append(s)

        for val in hashAnagram.values():
            result.append(val)
        return result