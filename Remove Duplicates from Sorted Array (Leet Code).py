class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[0:i]:
                nums[i]="_"
        while "_" in nums:
            nums.remove("_")
        return(len(nums))