class Solution(object):
    def isMonotonic(self, nums):
        temp = sorted(nums)
        temp2 = temp[::-1]
        if(temp==nums or temp2==nums):
            return True
        else:
            return False
        