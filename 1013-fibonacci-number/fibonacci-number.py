class Solution(object):
    def fib(self, n):
        if n<=1:
            return n
        l = self.fib(n-1)
        sl = self.fib(n-2)
        return sl+l

        