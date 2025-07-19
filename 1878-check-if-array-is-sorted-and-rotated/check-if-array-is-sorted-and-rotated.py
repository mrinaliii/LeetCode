from collections import deque
class Solution(object):
    def check(self, nums):
        temp = sorted(nums)
        nums = deque(nums)
        x = 0
        while x!=len(nums):
            nums.rotate(-1)
            if(list(nums)==temp):
                return True
            else:
                x+=1
        return False
        