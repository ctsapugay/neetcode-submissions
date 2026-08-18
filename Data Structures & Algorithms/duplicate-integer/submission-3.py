class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = nums.copy()
        for element in nums:
            # print(element, end='')
            # print("is in nums")
            nums2.remove(element)
            # print(nums)
            if element in nums2:
                return True
        return False
        