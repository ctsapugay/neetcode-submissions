class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = []
        suffix = []
        result = []
        prefix_prod = 1
        suffix_prod = 1
        for i in range(length):
            prefix_prod *= nums[i]
            prefix.append(prefix_prod)
            suffix_prod *= nums[length - 1 - i]
            suffix.append(suffix_prod)
        for i in range(length):
            if i == 0:
                result.append(suffix[length - 2])
            elif i == length - 1:
                result.append(prefix[length - 2])
            else:
                result.append(prefix[i-1] * suffix[length - i - 2])
        return result
        