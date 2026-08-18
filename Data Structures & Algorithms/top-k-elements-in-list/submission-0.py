class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        buckets = [[] for i in range(len(nums) + 1)]

        for item in nums:
            frequencies[item] = frequencies.get(item, 0) + 1
        for item, freq in frequencies.items():
            buckets[freq].append(item)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        