class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        old_dp = [False for i in range(0, m+1)]

        for a in A: 
            dp =[od for od in old_dp]
            for i in range(0, m+1):
                if old_dp[i] == True:
                    v = i+a
                    if v <= m:
                        dp[i+a] = True
            if a <= m:
                dp[a] = True
            print a, [i for i in range(0, len(dp)) if dp[i] == True]
            old_dp = dp

        for i in range(m, -1, -1):
            if dp[i] == True:
                return i



input = [12,3,7,4,5,13,2,8,4,7,6,5,7]
m = 90

cases = [(10, [3,4,8,5]), (m, input)]

so = Solution()
for m, input in cases:
    print so.backPack(m, input)