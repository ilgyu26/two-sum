from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    num_index = {}

    for index, num in enumerate(nums):
        num2 = target - num
        
        if num2 in num_index:
            return [num_index[num2], index]

        num_index[num] = index
