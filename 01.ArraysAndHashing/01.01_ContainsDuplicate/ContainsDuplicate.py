# Contains Duplicate
# LeetCode Problem 217
from typing import List
"""
Solution 1: Brute Force
1. iterate through array using 2 nested loops to check all distinct pairs of indices
2. if any pair of elements are equal, return True
3. if all pairs checked and no duplicates found, return False

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

"""
Solution 2: Sorting
1. sort the array in non-decreasing order
2. iterate through the array starting from index 1
3. compare the current element with the previous element
4. if both elements are equal, we have found a duplicate — return true
5. if the loop finishes without detecting equal neighbors, return false

Time Complexity: O(n log n)
Space Complexity: O(1) or O(n) depending on the sorting algorithm used
"""
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)): 
            if nums[i] == nums[i - 1]:
                return True
        return False

"""
Solution 3: Hash Set
1. initialize an empty hash set to store seen values
2. Iterate through each number in the array
3. For each number:
    - If it is already in the set, return true because a duplicate has been found
    - Otherwise, add it to the set
4. If the loop finishes without finding any duplicates, return false

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen: 
                return True
            seen.add(num)
        return False

"""
Solution 4: Hash Set Length
1. convert array into a hash set, removing duplicates
2. compare size of set with size of original array
3. if set is smaller, return true because duplicates were removed
4. otherwise, return false

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)