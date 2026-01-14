# Valid Anagram
# LeetCode Problem 242
from collections import Counter

from typing import List
"""
Solution 1: Sorting
1. if length of 2 strings differs, return False immediately
2. sort both strings
3. compare sorted version of strings

Time Complexity: O(nlogn + mlogm)
Space Complexity: O(1) or O(n + m) depending on the sorting algorithm used
"""
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

"""
Solution 2: Hash Map
1. if length of 2 strings differs, return False immediately
2. create 2 hash maps to store character frequencies for each string
3. iterate through both strings at same time:
    * increasing character count for s[i] in first map
    * increasing character count for t[i] in second map
4. after building both maps, compare them

Time Complexity: O(n + m)
Space Complexity: O(1), at most 26 characters
"""
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        return count_s == count_t

class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
Solution 3: Hash Map
1. if length of 2 strings differs, return False immediately
2. create frequency array count of size 26 initialised to 0
3. iterate through both strings at same time:
    * increasing count at index corresponding to s[i]
    * decreasing count at index corresponding to t[i]
4. scan through count array, and if any value not false return 0

Time Complexity: O(n + m)
Space Complexity: O(1)
"""
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord['a']] += 1
            count[ord(t[i]) - ord['a']] -= 1
        for num in count:
            if num != 0:
                return False
        return True