class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            # print("a")
            return False
        alphabet = dict()
        for letter in s:
            item = alphabet.get(letter, 0) + 1
            alphabet[letter] = item
        for letter in t:
            item = alphabet.get(letter, -1)
            if item > 1:
                alphabet[letter] = item - 1
            elif item <= -1:
                # print("b")
                return False
            else:
                alphabet.pop(letter)
        if len(alphabet) > 0:
            # print("c")
            return False
        return True
        