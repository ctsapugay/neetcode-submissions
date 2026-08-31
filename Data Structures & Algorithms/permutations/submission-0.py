class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(result, pre, leftover):
            # base case: only one option left
            if len(leftover) == 1:
                pre.append(leftover[0])
                result.append(pre.copy())
                return
            
            # >= 2 options left
            for i in range(len(leftover)):
                pre.append(leftover[i])
                if i == len(leftover) - 1:
                    dfs(result, pre.copy(), leftover[0:i])
                else:
                    dfs(result, pre.copy(), leftover[0:i] + leftover[i+1:])
                pre.pop()

            return

        dfs(result, [], nums)
        return result
        