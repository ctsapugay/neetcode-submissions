from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            # make the alphabet id
            alphabet_id = [0] * 26
            for letter in word:
                index = ord(letter) - 97
                alphabet_id[index] = alphabet_id[index] + 1
            hashmap[tuple(alphabet_id)].append(word)
        result = []
        for key in hashmap:
            result.append(hashmap[key])
        return result
            