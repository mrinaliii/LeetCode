class Solution(object):
    def heightChecker(self, heights):
        temp = sorted(heights)
        count = 0
        i = 0
        while(i!=len(heights)):
            if(temp[i]!=heights[i]):
                count+=1
            i+=1
        return count

        