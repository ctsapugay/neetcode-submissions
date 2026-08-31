class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case
        subproblems = [[]]

        # for every subproblem
        # insert first element into all indice
        for n in nums:
            new_problems = []
            for p in subproblems:
                for i in range(len(p) + 1):
                    pc = p.copy()
                    pc.insert(i, n)
                    new_problems.append(pc)
            subproblems = new_problems
        return subproblems

        