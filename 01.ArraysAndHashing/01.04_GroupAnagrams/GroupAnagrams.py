# Group Anagrams
# LeetCode Problem 49
from typing import List
from collections import defaultdict
"""
Solution 1: Sorting
1. create a hash map where each key is sorted version of string, and value is list of strings belonging to that anagram group
2. iterate through each string in input list:
   * sort characters to form key
   * append original string to list corresponding to key
3. after processing all string, return all values from hash map, which represent grouped anagrams

Time Complexity: O(m * n log n), m # strings, n length of longest string
Space Complexity: O(m * n)
"""
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # when defaultdict encounters key for 1st time, entry automatically created using default_factory, which in this case returns empty list
        res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)
        return list(res.values())

"""
Solution 2: Hash Table
1. create a hash map where each key is 26 length tuple representing character frequencies, and each value is list of strings belonging to that anagram group
2. for each string in input
   * initialise a count array of 26 0s
   * for each character c in string, increment count of corresponding index
   * convert count array to a tuple, and use as a key
   * append string to list associated with this key
3. after processing all strings, return all lists stored in hash map

Time Complexity: O(m * n), m # strings, n length of longest string
Space Complexity: O(m * n)
"""
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # when defaultdict encounters key for 1st time, entry automatically created using default_factory, which in this case returns empty list
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())
