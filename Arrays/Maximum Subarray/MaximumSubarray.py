def maxSubArray(self, nums: List[int]) -> int:
    # Kadanes Algorithm
    # check is it better to start of from a new number from position x or keep the previous values
    cursum = nums[0]
    maxsum = nums[0]
    for x in range(1, len(nums)):
        cursum = max(nums[x]+cursum, nums[x])
        maxsum = max(maxsum, cursum)
    return maxsum
