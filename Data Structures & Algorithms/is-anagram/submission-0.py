class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = dict()
        for letter in s:
            try:
                item = alphabet.pop(letter)
                alphabet[letter] = item + 1
            except:
                alphabet[letter] = 1
        for letter in t:
            try:
                item = alphabet.pop(letter)
                if item > 1:
                    alphabet[letter] = item - 1
            except:
                return False
        if len(alphabet) > 0:
            return False
        return True
        