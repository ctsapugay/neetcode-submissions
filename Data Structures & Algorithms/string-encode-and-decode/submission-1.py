class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        result = ""
        for word in strs:
            result += word
            result += '\0'
        return result

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