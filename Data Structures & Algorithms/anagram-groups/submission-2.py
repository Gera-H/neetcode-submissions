class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupHash = {}

        for s in strs:
            temp = "".join(sorted(s))
            if temp in groupHash:
                groupHash[temp].append(s)
            else:
                groupHash[temp] = [s]

        return list(groupHash.values())