class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def step(lefts, rights, string):
            # provided you have some pre string "(()... "
            # based on number of each end remaining
            # decide what to add

            # base case: none left
            if lefts == rights == 0:
                result.append("".join(string))
                return
            
            # must always have remaining lefts <= rights
            if lefts == rights: # use left
                string.append("(")
                step(lefts - 1, rights, string)
                string.pop()
            
            elif lefts == 0: # only rights left
                string.append(")")
                step(lefts, rights - 1, string)
                string.pop()
            
            else: # anything goes --> branch
                string.append("(")
                step(lefts - 1, rights, string)
                string.pop()
            
                string.append(")") # use right
                step(lefts, rights - 1, string)
                string.pop()

        step(n, n, [])
        return result