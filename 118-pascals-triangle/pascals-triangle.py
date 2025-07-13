class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            if i==0:
                res.append([1])
            elif i==1:
                res.append([1,1])
            else:
                prev = res[-1]
                new = [1]
                for j in range(1, len(prev)):
                    new.append(prev[j-1]+prev[j])
                new.append(1)
                res.append(new)
        return res
                    
        