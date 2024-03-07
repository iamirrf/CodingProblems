class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Create a dictionary to hold number to index mapping
        for index, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            if complement in num_map:
                return [num_map[complement], index]  # Return the indices
            num_map[num] = index  # Add the current number to the dictionary
