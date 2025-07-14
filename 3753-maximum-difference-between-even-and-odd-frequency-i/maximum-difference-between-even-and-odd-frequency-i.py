class Solution(object):
    def maxDifference(self, s):
        temp = list(s)
        d = dict.fromkeys(temp, 0)
        for i in s:
            d[i] += 1
        e = 99999
        o = 0
        for i in (d):
            if (d[i] % 2 == 0):
                e = min(e, d[i])
            else:
                o = max(o, d[i])
        return o-e
        