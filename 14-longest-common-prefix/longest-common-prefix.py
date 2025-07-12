class Solution(object):
    def longestCommonPrefix(self, strs):
        if(len(strs)==0):
            return ""
        temp = strs[0]
        for i in strs[1:]:
            j = 0
            while(j<len(temp) and j<len(i) and temp[j]==i[j]):
                j+=1
            temp = temp[:j]
            if(temp == ""):
                break
        return temp

        # m = min(len(s) for s in strs)
        # for i in range(m):
        #     temp = strs[0][i]
        #     for j in strs[1:]:
        #         if(j[i]!=temp):
        #             break