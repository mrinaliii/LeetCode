class Solution(object):
    def iseven(self, n):
        return n % 2 == 0
    
    def isodd(self, n):
        return n % 2 != 0
        
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        
        for i in range(len(nums) - 1):
            if (self.iseven(nums[i]) and self.iseven(nums[i + 1])) or \
               (self.isodd(nums[i]) and self.isodd(nums[i + 1])):
                return False
        return True