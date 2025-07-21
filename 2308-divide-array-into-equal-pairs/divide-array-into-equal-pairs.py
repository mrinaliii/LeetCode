class Solution(object):
    def divideArray(self, nums):
        temp = sorted(nums)
        d = {}
        for i in temp:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for j in d.values():
            if(j%2!=0):
                return False
        return True
        