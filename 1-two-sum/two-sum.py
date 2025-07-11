class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i,j in enumerate(nums):
            x = target - j
            if x in dict:
                return[dict[x], i]
            dict[j] = i
        return []
