class Solution(object):
    def replaceElements(self, arr):
        temp = list(arr)
        max1 = arr[-1]
        i = len(arr)-2
        j = len(arr)-1
        while(i>=0):
            temp[i] = max1
            i -= 1
            j -= 1
            max1 = max(max1, arr[j])
        temp[-1]=-1
        return temp
        