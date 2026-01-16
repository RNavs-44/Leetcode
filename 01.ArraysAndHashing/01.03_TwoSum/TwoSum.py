# Two Sum
# LeetCode Problem 1

"""
Solution 1: Brute Force
1. iterate through the array with two nested loops using indices i and j to check every pair of different elements
2. if the sum of the pair equals the target, return the indices of the pair
3. if no such pair is found, return an empty array
4. there is guaranteed to be exactly one solution, so we will never return an empty array

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
from typing import List
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

"""
Solution 2: Sorting
1. create a copy of the array and sort it in descending order
2. initialise 2 pointers, 1: i at the beginning and 2: j at the end
3. iterate through array with 2 pointers and check if sum of the 2 numbers equal to the target
4. if sum equal to target, return indices of 2 pointers
   if sum less than target, move left pointer i to the right, increasing the sum
   if sum greater than target, move right pointer j to the left, decreasing the sum
5. guaranteed to be exactly 1 solution so will never return empty array


Time Complexity: O(n log n)
Space Complexity: O(n)
"""
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i, num in enumerate(nums):
            a.append([num, i])
        a.sort()
        i, j = 0, len(a) - 1
        while i < j:
            sum = a[i][0] + a[j][0]
            if sum == target:
                return [a[i][1], a[j][1]]
            elif sum < target:
                i += 1
            else:
                j -= 1
        return []


"""
Solution 3: Hash Map (2 passes)
1. create a hash map to store value and index of each element
2. iterate through array and compute complement of current element, which is target - nums[i]
3. check if complement exists in hash map
4. if it does, return indices of current array and hashmap
   if it doesn't, return empty array

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # val -> index
        for i, n in enumerate(nums):
            indices[n] = i
        for i, n in enumerate(nums):
            complement = target - n
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]
        return []

"""
Solution 4: Hash Map (1 pass)
1. create a hash map to store value and index of each element
2. iterate through array using index i and compute complement of current element
3. check if complement exists in hash map
4. if it does, return indices of current array and hashmap
   if it doesn't, return empty array

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # val -> index

        for i, n in enumerate(nums):
            complement = target - n
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]
            indices[n] = i
        return []