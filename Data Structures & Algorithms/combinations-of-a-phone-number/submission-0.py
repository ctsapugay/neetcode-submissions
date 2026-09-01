class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []

        translation = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }

        result = []
        def dfs(pre, d):
            nonlocal translation

            # base case
            if d >= len(digits):
                # reached a leaf node
                result.append("".join(pre))
                return

            for l in range(len(translation[int(digits[d])])):
                # branch for each associated letter
                pre.append(translation[int(digits[d])][l])
                dfs(pre.copy(), d+1)
                pre.pop()
            
            return
        
        dfs([], 0)
        return result
        