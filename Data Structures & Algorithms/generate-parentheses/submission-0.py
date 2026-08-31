class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def step(lefts, rights, string):
            # provided you have some pre string "(()... "
            # based on number of each end remaining
            # decide what to add

            # base case: none left
            if lefts == rights == 0:
                result.append(string)
                return
            
            # must always have remaining lefts <= rights
            if lefts == rights: # use left
                step(lefts - 1, rights, string + "(")
            elif lefts == 0: # only rights left
                step(lefts, rights - 1, string + ")")
            else: # anything goes --> branch
                step(lefts - 1, rights, string + "(")
                step(lefts, rights - 1, string + ")")

        step(n, n, "")
        return result