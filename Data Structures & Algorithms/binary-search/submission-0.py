class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            midpt = int((end - start) / 2) + start
            if nums[midpt] < target:
                start = midpt + 1
                print(f"start: {nums[midpt]}")
            elif nums[midpt] > target:
                end = midpt - 1
                print(f"end: {nums[midpt]}")
            elif nums[midpt] == target:
                return midpt
        return -1

        