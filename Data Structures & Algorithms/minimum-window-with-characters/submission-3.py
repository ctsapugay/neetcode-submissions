class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        count = {}
        for c in t:
            target[c] = target.get(c, 0) + 1

        targets_met = 0
        l = 0
        while l < len(s) and target.get(s[l], 0) == 0:
            # iterate until end of possible sequence or hit valid char
            if len(s) - l < len(t):
                return ""
            l += 1
        
        if l >= len(s) or target.get(s[l], 0) == 0:
            return ""

        # print("a")
        start = 0
        end = float('inf')
        for r in range(l, len(s)):
            if target.get(s[r], 0) == 0:
                continue

            count[s[r]] = count.get(s[r], 0) + 1
            if count[s[r]] <= target[s[r]]:
                targets_met += 1
            while targets_met >= len(t): # valid substring
                # print("b")
                if r-l < end-start: # if window is smaller save it
                    start = l
                    end = r
                count[s[l]] -= 1 # decrement the count of the item removed
                if count[s[l]] < target[s[l]]: # update validation
                    targets_met -= 1
                # move l to next significant character
                l += 1
                while l < r and target.get(s[l], 0) == 0:
                    if len(s) - l < len(t):
                        return end - start
                    l += 1
        
        if end == float('inf'):
            return ""
        return s[start:end+1]

        