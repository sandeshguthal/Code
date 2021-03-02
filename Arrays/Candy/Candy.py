def candy(self, ratings: List[int]) -> int:
    rewards = [1 for x in range(len(ratings))]
    for x in range(1, len(ratings)):
        if ratings[x] > ratings[x-1]:
            rewards[x] = max(rewards[x-1]+1, rewards[x])
    print(rewards)
    for y in range(len(ratings)-2, -1, -1):
        if ratings[y] > ratings[y+1]:
            rewards[y] = max(rewards[y+1]+1, rewards[y])
    print(rewards)
    total = 0
    for x in rewards:
        total += x
    return total
