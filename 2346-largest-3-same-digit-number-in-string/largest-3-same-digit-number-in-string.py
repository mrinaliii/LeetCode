class Solution(object):
    def largestGoodInteger(self, num):
        temp = []
        n = list(num)
        print(n)
        for i in range(len(n)-2):
            if n[i] == n[i+1]:
                if n[i+1]==n[i+2]:
                    temp.append(num[i:i+3])
        if temp:
            return max(temp)  
        else:
            return ""                  
        