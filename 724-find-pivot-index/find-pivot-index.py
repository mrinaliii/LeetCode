class Solution(object):
    def pivotIndex(self, nums):
        tot = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            rsum = tot - lsum - nums[i]
            if(rsum==lsum):
                return i
            else:
                lsum+=nums[i]
        return -1
        # for i in range(len(nums)):
        #     j = i-1
        #     k = i+1
        #     lsum = rsum = 0
        #     while j>=0:
        #         lsum += nums[j]
        #         j-=1
        #     while k<=len(nums)-1:
        #         rsum += nums[k]
        #         k+=1
        #     if(lsum == rsum):
        #         return i
        # return -1
        