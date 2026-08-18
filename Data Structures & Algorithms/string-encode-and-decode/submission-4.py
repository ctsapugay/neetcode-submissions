class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(word) 
            result.append('\0')
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        word = ""
        result = []
        for char in s:
            if char != '\0':
                word += char
            else:
                result.append(word)
                word = ""
        return result