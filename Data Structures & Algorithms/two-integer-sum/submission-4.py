from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
            try:
                for j in hashmap[target - nums[i]]:
                    if j != i:
                        return [min(i, j), max(i, j)]
            except:
                pass

        