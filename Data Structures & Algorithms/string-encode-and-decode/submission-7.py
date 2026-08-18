class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = []
        for word in strs:
            result.append(str(len(word)))
            result.append('#')
            result.append(word)
        answer = ''.join(result)
        print(answer)
        return answer

    def decode(self, s: str) -> List[str]:
        sizes, result = [], []
        if not s:
            return []
        i = 0
        while i < len(s):
            if s[i] != '#':
                sizes.append(s[i])
            else:
                start = i+1
                i += int(''.join(sizes))
                result.append(s[start:i+1])
                sizes = []
            i += 1
        return result



