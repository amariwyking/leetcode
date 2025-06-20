from typing import List

def mostWater(height: List[int]):
    max_area = 0
    
    for i in range(len(height)):
        for j in range(len(height)):
            calc_area = abs(i-j) * min(height[i], height[j])
            
            max_area = max(max_area, calc_area)
            
    return max_area

print(mostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))

print(mostWater([10000, 10]))