from scoring.simple import GAP

def initialize_matrix(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # fill first column
    for i in range(n + 1):
        dp[i][0] = i * GAP

    # fill first row
    for j in range(m + 1):
        dp[0][j] = j * GAP

    return dp
from scoring.simple import score, GAP

def fill_matrix(dp, seq1, seq2):
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):

            match = dp[i-1][j-1] + score(seq1[i-1], seq2[j-1])
            delete = dp[i-1][j] + GAP
            insert = dp[i][j-1] + GAP

            dp[i][j] = max(match, delete, insert)

    return dp