class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        highest = 0
        for x in range(1, len(arr)-1):
            if arr[x-1] < arr[x] and arr[x+1] < arr[x]:
                left = x
                right = x
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                while right < len(arr)-1 and arr[right+1] < arr[right]:
                    right += 1
                highest = max(right-left+1, highest)
        return highest
