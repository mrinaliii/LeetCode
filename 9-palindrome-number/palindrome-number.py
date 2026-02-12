class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            x2 = x
            d = 0
            while x>0:
                d = d*10+(x%10)
                x//=10
            if d<=-2**31 or d>=2**31:
                return False
            else:
                return True if x2==d else False
        