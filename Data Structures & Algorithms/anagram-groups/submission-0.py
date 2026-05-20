class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashCount = defaultdict(list)
        
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j)-ord("a")] += 1
            hashCount[tuple(count)].append(i)

        print(hashCount.values())
        return hashCount.values()