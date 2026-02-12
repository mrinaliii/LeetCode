class Solution(object):
    def reverse(self, x):
        x1 = str(x)
        x2 = []
        
        if x < 0:
            x2.append("-")
            for i in range(len(x1)-1, 0, -1):
                x2.append(x1[i])
        else:
            for i in range(len(x1)-1, -1, -1):
                x2.append(x1[i])
        x=int("".join(x2))
        if x>=2**31-1 or x<=-2**31:
            return 0
        else:
            return x
