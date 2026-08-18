class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starters = ['(', '[', '{']
        grammar = {}
        grammar[')'] = '('
        grammar[']'] = '['
        grammar['}'] = '{'
        for c in s:
            if c in starters:
                stack.append(c)
            elif len(stack) <= 0:
                return False
            elif grammar[c] != stack.pop():
                return False
        if len(stack) == 0:
            return True
        return False



        