class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        result = [0] * n
        prefix[0] = 1
        suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[n - 1 - i] = suffix[n - i] * nums[n - i]
            # print(f"{i}: {prefix[i]}, {suffix[i]}")
        # print(suffix)
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result

        