class Solution(object):
    def maxNumberOfBalloons(self, text):
        char_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in char_count:
                char_count[char] += 1
        return min(
            char_count['b'],      
            char_count['a'],      
            char_count['l'] // 2,
            char_count['o'] // 2, 
            char_count['n']       
        )