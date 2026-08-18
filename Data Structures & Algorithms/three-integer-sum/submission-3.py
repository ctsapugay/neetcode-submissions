class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        while i < len(nums):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if -nums[i] == nums[j] + nums[k]:
                    result.append([nums[i], nums[j], nums[k]])
                    # go to the next unique j
                    j += 1
                    while (j < k) and (nums[j] == nums[j-1]):
                        j += 1
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                elif -nums[i] < nums[j] + nums[k]:
                    k -= 1
            # go to the next unique i
            i += 1
            while (i < len(nums)) and (nums[i] == nums[i-1]):
                i += 1
        return result