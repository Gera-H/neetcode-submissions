class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        n = len(nums)
        output = []
        count = 0

        for i in range(n):
            frequency[nums[i]] = 1 + frequency.get(nums[i],0)

        frequency = sorted(frequency.items(), key=lambda x: x[1],reverse=True)

        for key,_ in frequency:
            if count == k:
                break
            output.append(key)
            count += 1
        return output