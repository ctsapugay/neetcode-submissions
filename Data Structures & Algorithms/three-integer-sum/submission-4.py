class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if (i > 0) and (a == nums[i-1]):
                continue
            
            j, k = i+1, len(nums)-1
            while j < k:
                threeSum = a + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                elif threeSum == 0:
                    result.append([a, nums[j], nums[k]])
                    j += 1
                    while (j < k) and (nums[j] == nums[j-1]):
                        j += 1
        return result
        