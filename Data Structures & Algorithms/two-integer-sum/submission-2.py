class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            try:
                second = nums.index(target - nums[first])
                if first != second:
                    if first < second:
                        result = [first, second]
                        return result
                    else:
                        result = [second, first]
                        return result
            except:
                pass  
        