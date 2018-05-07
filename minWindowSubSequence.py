class Solution:
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        M = len(S)
        N = len(T)
        dp = [[-1 for _ in range(N + 1)] for _ in range(M + 1)]  # DP is M+1 x N+1
        min_len = float('inf')
        start = -1
        # dp[i][j] is the INDEX POSITION of S that covers the first j characters of T within the first i characters of S.

        # Initialize DP first column of DP (the extra row + the first extra column)
        for i in range(M):
            dp[i][
                0] = i  # DP[3][0] means the starting position is 3 to cover the first 0 chars of T (nothing), within the first 3 chars of S. So starting positoin of 3 here refers to NOTHING.

        # Fill each element of DP
        for i in range(1, M+1):
            for j in range(1,N+1):
                if S[i - 1] == T[j - 1]:  # S[i-1] refers to the correspoinding element in S, because DP has one extra element.
                    dp[i][j] = dp[i - 1][j - 1]  # If last digit of S is same as last digit of T, then the starting position is same as the when S and T are both at its previous char.
                else:
                    dp[i][j] = dp[i - 1][j]  # If not the same, then starting position is same as when S has one less char.

            if dp[i][N] != -1:  # If the entire T has been covered with a given S[i-1]:
                length = i-dp[i][N]
                if length < min_len:
                    min_len = length
                    start = dp[i][N]

        return S[start:start + min_len] if start!=-1 else ""


