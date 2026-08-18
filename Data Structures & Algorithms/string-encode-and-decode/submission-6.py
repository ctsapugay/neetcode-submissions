class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(word) 
            result.append('\0')
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        for idx, char in enumerate(s):
            if char == '\0':
                result.append(s[start:idx])
                start = idx + 1
        return result
