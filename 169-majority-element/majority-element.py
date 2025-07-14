class Solution(object):
    def majorityElement(self, nums):
        d = dict.fromkeys(nums, 0)
        print(d)
        for i in nums:
            d[i] += 1
        for i in d:
            if d[i]>len(nums)/2:
                return i
                
