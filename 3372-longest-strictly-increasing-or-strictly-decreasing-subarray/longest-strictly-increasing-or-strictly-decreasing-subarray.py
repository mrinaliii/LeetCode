class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc = 0
        inc = dec = res = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            res = max(res, inc, dec)

        return res   