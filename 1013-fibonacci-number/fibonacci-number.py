class Solution(object):
    def fib(self, n, memo={}):
        if n in memo:
            return memo[n]
        if n<=1:
            return n
        memo[n]=self.fib(n-1,memo)+self.fib(n-2,memo)
        return memo[n]

        