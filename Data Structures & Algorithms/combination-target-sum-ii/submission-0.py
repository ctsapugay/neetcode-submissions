class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtracking(currSum, currArr, index):
            if currSum == target:
                result.append(currArr.copy())
                # print(f"{currArr} --> {currSum}")
                return
            if currSum > target or index >= len(candidates): 
                # sum exceeds target or out of range
                # print(currArr)
                return 

            # currSum is less than target
            # we can add, or not add, the next element

            # add the element at index
            currArr.append(candidates[index])
            backtracking(currSum + candidates[index], currArr, index + 1)

            # skip the element at index
            item = currArr.pop()
            while index < len(candidates) and candidates[index] == item:
                # in range dupe detected
                index += 1
            backtracking(currSum, currArr, index)

            # print(currArr)
            return
        
        backtracking(0, [], 0)
        return result
