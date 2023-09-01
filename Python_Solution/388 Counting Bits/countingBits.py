class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)                    #creating a list of size (n+1) and assigning all values to 0
        offset = 1                            
        for i in range(1, n + 1):
            if offset*2 == i:
                offset=i
            dp[i] = 1 + dp[i - offset]
        return dp
