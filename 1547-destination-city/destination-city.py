class Solution(object):
    def destCity(self, paths):
        s = {p[0] for p in paths}
        for i in paths:
            if(i[1] not in s):
                return i[1]
        # t = paths[0]
        # x = t[0]
        # y = t[1]
        # count = 0
        # for i in range(1, len(paths)):
        #     x1 = paths[i]
        #     y1 = x1[0]
        #     if(y1 == y):
        #         y = y1
        #         count = i
        #     else:
        #         continue
        # x1 = paths[count]
        # y1 = x1[1]
        # return y1