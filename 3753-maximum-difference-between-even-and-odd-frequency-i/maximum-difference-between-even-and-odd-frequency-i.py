class Solution(object):
    def maxDifference(self, s):
        d = dict.fromkeys(s, 0)
        print(d)
        for i in s:
            d[i] += 1
        e = []
        o =[]
        for i in (d.values()):
            if (i % 2 == 0):
                e.append(i)
            else:
                o.append(i)
        x = max(o)
        y = min(e)
        return x-y
        