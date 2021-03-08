def minDistance(self, word1: str, word2: str) -> int:
    def dist(index1, index2, memo):
        insert = 0
        delete = 0
        replace = 0

        if index1 >= len(word1) and index2 >= len(word2):
            return 0
        if index1 >= len(word1) and index2 < len(word2):
            return 1 + dist(index1, index2+1, memo)

        if index1 < len(word1) and index2 >= len(word2):
            return 1 + dist(index1+1, index2, memo)

        if memo[index1][index2] != 2**31:
            return memo[index1][index2]

        if word1[index1] == word2[index2]:
            return dist(index1+1, index2+1, memo)

        replace = 1 + dist(index1+1, index2+1, memo)
        delete = 1 + dist(index1+1, index2, memo)
        insert = 1 + dist(index1, index2+1, memo)
        memo[index1][index2] = min(replace, delete, insert)
        return memo[index1][index2]
    memo = []
    for x in range(len(word1)):
        memo.append([])
        for y in range(len(word2)):
            memo[x].append(2**31)
    return dist(0, 0, memo)
