from scoring.simple import score, GAP

def initialize_matrix(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    return dp

def fill_matrix(dp, seq1, seq2):
    max_score = 0
    max_pos = (0, 0)

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):

            match = dp[i-1][j-1] + score(seq1[i-1], seq2[j-1])
            delete = dp[i-1][j] + GAP
            insert = dp[i][j-1] + GAP

            dp[i][j] = max(0, match, delete, insert)

            # track best cell
            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_pos = (i, j)

    return dp, max_pos

