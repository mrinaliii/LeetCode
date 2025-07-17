class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        map = {}
        for c, w in zip(pattern, words):
            if c not in map:
                if w in map.values():
                    return False
                map[c] = w
            elif map[c] != w:
                return False
        
        return True