class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result, l, maxf = 0, 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r-l+1)
        return result
            