class NumArray(object):

    def __init__(self, nums):
        self.temp = []
        for i in nums:
            self.temp.append(i)

    def sumRange(self, left, right):
        sum = 0
        for i in range(left, right+1):
            sum+=self.temp[i]
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)