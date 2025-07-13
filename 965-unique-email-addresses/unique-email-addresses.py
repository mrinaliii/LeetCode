class Solution(object):
    def numUniqueEmails(self, emails):
        temp = set()
        for i in emails:
            name,dom = i.split('@')
            x = ""
            for j in name:
                if j == ".":
                    continue
                elif j == "+":
                    break
                else:
                    x+=j
            y = x+"@"+dom
            temp.add(y)
        return len(temp)
        