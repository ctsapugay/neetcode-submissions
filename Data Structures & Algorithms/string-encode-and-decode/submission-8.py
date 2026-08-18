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
        if not s:
            return []
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            result.append(s[j:j+length])
            i = j + length
        return result
            



