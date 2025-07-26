class Solution(object):
    def maxProductDifference(self, nums):
        m = sorted(nums)
        m1 = m[len(m)-1]
        m2 = m[len(m)-2]
        m3 = m[1]
        m4 = m[0]
        return (m1*m2) - (m3*m4)