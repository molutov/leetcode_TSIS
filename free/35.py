# by Bekzat
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: return nums.index(target)
        else:
            for i in range(len(nums)):
                if target > nums[len(nums) - 1]: return len(nums)
                elif target < nums[0]: return 0
                elif target < nums[i]: return i
        
