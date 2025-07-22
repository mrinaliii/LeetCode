class Solution(object):
    def getRow(self, rowIndex):
        temp = []
        for i in range(rowIndex+1):
            if(i == 0):
                temp.append([1])
            elif(i == 1):
                temp.append([1,1])
            else:
                prev = temp[-1]
                new = [1]
                for j in range(1, len(prev)):
                    new.append(prev[j-1]+prev[j])
                new.append(1)
                temp.append(new)
        return temp[rowIndex]