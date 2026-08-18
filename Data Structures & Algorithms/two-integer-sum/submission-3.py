class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            try:
                second = nums.index(target - nums[first])
                if first != second:
                    return [min(first, second), max(first, second)]
            except:
                pass  
        