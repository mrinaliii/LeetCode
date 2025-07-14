class Solution(object):
    def maxAscendingSum(self, nums):
        mx = temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += nums[i]
            else:
                temp = nums[i] 
            mx = max(mx, temp)
        return mx

        