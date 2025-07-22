class Solution(object):
    def countCharacters(self, words, chars):
        count = 0
        for i in words:
            temp = 0
            temp1 = list(chars)
            for j in i:
                if j in temp1:
                    temp1.remove(j) 
                    temp += 1
                else:
                    break 
            if temp == len(i):
                count += temp
        return count