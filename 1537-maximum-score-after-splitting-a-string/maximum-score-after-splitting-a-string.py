class Solution(object):
    def maxScore(self, s):
        S = list(s)
        count = 0
        i = 0
        while(i!=len(S)-1):
            m = n = 0
            for j in range(0, i+1):
                if(S[j]=='0'):
                    m+=1
            for k in range(i+1, len(S)):
                if(S[k]=='1'):
                    n+=1
            count = max(count, m+n)
            i+=1
        return count
        