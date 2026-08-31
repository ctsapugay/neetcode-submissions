class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) == 0: return [[]]

        # for every subproblem
        # insert first element into all indices
        subproblems = self.permute(nums[1:])
        result = []
        for p in subproblems:
            for i in range(len(p) + 1):
                pc = p.copy()
                pc.insert(i, nums[0])
                result.append(pc)

        return result