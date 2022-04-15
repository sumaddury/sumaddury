class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        using_range=range(0,len(nums))
        for i in using_range:
            for i2 in using_range:
                if (nums[i]+nums[i2]==target) and not (i==i2):
                    return(i,i2)