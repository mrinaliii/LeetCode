class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1+i, len(nums)):
                if(target==nums[i]+nums[j]):
                    return [i,j]
        return []

        