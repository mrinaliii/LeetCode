class Solution(object):
    def countSeniors(self, details):
        count = 0
        for i in range(len(details)):
            temp = list(details[i])
            x = (int(temp[-4])*10)+(int(temp[-3]))
            if(x>60):
                count+=1
        return count

        