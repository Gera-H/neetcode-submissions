class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = {}


        for i in range(len(nums)): 
            hashCount[nums[i]] = 1 + hashCount.get(nums[i],0)
        print(hashCount) 
        
        res = [] 
        hashCount = dict(sorted(hashCount.items(), key=lambda item: item[1], reverse=True))
        
        for i in enumerate(hashCount):
            if i[0] < k:
                
                res.append(i[1])
        return res