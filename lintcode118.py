class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        ls = len(S)
        lt = len(T)
        
        if lt == 0:
            return 1
            
        if ls < lt:
            return 0
        
        dp = [[0 for i in range(0, ls)] for j in range(0, lt)] 
        
        dp[0][0] = 1 if T[0] == S[0] else 0
#        for r in range(1, lt):
#            dp[r][0] = 1 if T[r] == S[0] else dp[r-1][0]
            
        for c in range(1, ls):
            dp[0][c] = dp[0][c-1] + (1 if S[c] == T[0] else 0)
            
        print ' [', ', '.join(S), ']'
        for i, line in enumerate(dp):
            print T[i], line

        print

        for i in range(1, lt):
            for j in range(1, ls):
                dp[i][j] = dp[i][j-1]
                if T[i] == S[j]:                   
                    dp[i][j] += dp[i-1][j-1]
                    
        print ' [', ', '.join(S), ']'
        for i, line in enumerate(dp):
            print T[i], line

        return dp[-1][-1]

s = Solution()
print s.numDistinct('anacondastreetracecar', 'contra')