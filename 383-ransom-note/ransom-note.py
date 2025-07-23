class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r = list(ransomNote)
        m = list(magazine)
        print(r)
        print(m)
        for i in r:
            if i in m:
                m.remove(i)
            else:
                return False
        return True        