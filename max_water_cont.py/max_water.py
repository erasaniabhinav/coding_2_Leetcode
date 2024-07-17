# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36

height = [1,7,2,5,4,7,3,6]

#we will write a func to cal the max area
def max_area(height):
    max_area = 0
    l = 0
    r = len(height)-1


    while l < r:
        # using the formula 
        current_area = min(height[l],height[r]) * (r-l)
        # Update max_area if the current_area is larger
        max_area = max(max_area, current_area)


        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

print(max_area(height))





