class Solution(object):
    def wordPattern(self, pattern, s):
        temp = s.split()
        if len(pattern) != len(temp):
            return False
        
        d = {}
        for c, w in zip(pattern, temp):
            if c not in d:
                if w in d.values():
                    return False
                d[c] = w
            elif d[c] != w:
                return False
        
        return True