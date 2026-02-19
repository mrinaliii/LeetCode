class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        l=0
        tot=0
        mx = 0
        for r in range(len(nums)):
            tot+=nums[r]
            while nums[r]*(r-l+1)-tot>k:
                tot-=nums[l]
                l+=1
            mx = max(mx, r-l+1)
        return mx
            

        