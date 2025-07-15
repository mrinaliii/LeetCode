class Solution(object):
    def kthDistinct(self, arr, k):
        temp = {}
        for i in arr:
            if i in temp:
                temp[i].append(1)
            else:
                temp[i] = [1]
        temp2 = []
        for i in arr:
            if len(temp[i]) == 1:
                temp2.append(i)
        if k <= len(temp2):
            return temp2[k-1]
        else:
            return ""  