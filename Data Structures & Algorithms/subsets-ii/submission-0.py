class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(pre, i):
            if i >= len(nums): 
                result.append(pre[::])
                return

            # branch: include
            pre.append(nums[i])
            dfs(pre, i+1)
            pre.pop()

            # branch: do NOT include
            while i + 1 < len(nums) and nums[i] == nums[i+1]: # skip dupes
                i += 1
            dfs(pre.copy(), i+1)

            return

        dfs([], 0)
        return result
