class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        
        last_seen = {}
        last_seen[s[0]] = 0
        l, result = 0, 1

        for r in range(len(s)):
            if r <= l:
                continue
            if last_seen.get(s[r], -1) != -1:
                # seen before
                l = max(last_seen[s[r]] + 1, l)
            print(f"{l}, {r}")
            last_seen[s[r]] = r
            result = max(result, r-l+1)
            print(last_seen)
            print(result)
        return result