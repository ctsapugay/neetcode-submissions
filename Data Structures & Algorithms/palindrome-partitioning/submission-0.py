class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(array):
            l, r = 0, len(array) - 1
            while l < r:
                if array[l] != array[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(substrings, buffer, idx):
            # assume list of substrings contains palindromes
            # and buffer contains remaining chars up to idx

            # base case: whole string accounted for except buffer
            if idx >= len(s):
                if len(buffer) == 0: # whole string accounted
                    return
                if isPalindrome(buffer): # check buffer
                    substrings.append("".join(buffer))
                    result.append(substrings)
                    return
                return

            # add idx to buffer
            buffer.append(s[idx])

            # branch: add buffer as substring
            # if buffer is not palindrome --> prune
            if isPalindrome(buffer):
                substrings.append("".join(buffer))
                dfs(substrings.copy(), [], idx+1)
                substrings.pop()
            # branch: continue working on buffer
            dfs(substrings, buffer, idx+1)
            return

        dfs([], [], 0)
        return result
        