class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for i in strs:
                srt = "".join(sorted(i))
                if srt in res:
                    res[srt].append(i)
                else:
                    res[srt] = [i]
        return res.values()
        