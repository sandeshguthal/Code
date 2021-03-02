if len(height) == 0:
            return 0
        left = [0 for x in range(len(height))]
        right = [0 for x in range(len(height))]
        left[0]= height[0]
        right[len(height)-1] = height[len(height)-1]
        
        # check from left to right to check the largest value to the left at x position
        
        for x in range(1,len(height)):
            if height[x]>left[x-1]:
                left[x] = height[x]
            else:
                left[x] = left[x-1]
                
        # check from right to left to check the largest value to the right at x position
        for x in range(len(height)-2,-1,-1):
            if height[x] > right[x+1]:
                right[x] = height[x]
            else:
                right[x] = right[x+1]
        total = 0
        # water can only be filled to the minimum value either to the right or left and height[x] amount cannot be filled. Therefore -height[x]
        for x in range(len(height)):
            total+=min(left[x],right[x])-height[x]
        return total
