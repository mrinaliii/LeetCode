class Solution(object):
    def countConsistentStrings(self, allowed, words):
        x = list(allowed)
        count = 0
        for i in words:
            temp = 0
            for j in i:
                if j in x:
                    temp+=1
                else:
                    break
            if(len(i)==temp):
                count+=1
        return count
                                

        