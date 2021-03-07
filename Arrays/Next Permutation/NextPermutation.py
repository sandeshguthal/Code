def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    x = len(nums)-1
    while x > 0 and nums[x] <= nums[x-1]:
        x = x-1
    x = x-1
    y = len(nums)-1
    while y > -1 and nums[x] >= nums[y]:
        y -= 1
    if x >= 0:
        nums[y], nums[x] = nums[x], nums[y]

    def reverse(nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
    reverse(nums, x+1, len(nums)-1)
    return nums
