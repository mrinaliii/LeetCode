class Solution(object):
    def lengthOfLastWord(self, s):
        x = s.strip()
        char = 0
        count = 0
        if(len(s)==1):
            return 1
        else:
            for i in range(len(s)-1, -1, -1):
                if(s[i]==' ' and char==0):
                    continue
                elif(s[i]!=' '):
                    char+=1
                    count+=1
                else:
                    break
            return count

    
        