# Top K Frequent Elements
# LeetCode Problem 347

# Group Anagrams
# LeetCode Problem 49
from typing import List
from collections import defaultdict
import heapq
"""
Solution 1: Sorting
1. create a hash map to store frequency of each number
2. build a list of [frequency, number] pairs from map
3. sort list in ascending order based on frequency
4. create an empty result list
5. repeatedly pop from end of sorted list and append number to result
   stop when result contains k elements
6. return result list

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            # count[num] = count.get(num, 0)
        
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])

        # arr = [[cnt, num] for num, cnt in count.items()]

        # arr.sort(reverse=True)
        # res = list(map(lambda x: x[1], arr[:k]))
        # return res
        
        
        arr = list(map(list, count.items()))
        arr.sort(key=lambda x: x[1])

        res = []
        while len(res) < k:
            res.append(arr.pop()[0])
        return res

"""
Solution 2: Min Heap
1. build a frequency map that counts how many times each number appears
2. create an empty min-heap
3. for each number in frequency map:
    * push (frequency, number) into heap
    * if heap size > k then pop once to remove smallest frequency
4. after processing all numbers, heap contains k most frequent elements
5. pop all elements from heap and collect numbers in results list
6. return result

Time Complexity: O(n log k)
Space Complexity: O(n + k)
"""
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res

"""
Solution 3: Bucket Sort
1. build a frequency map that counts how many times each number appears
2. create a list of group freqs where freq[i] will store all numbers that appear exactly i times
3. for each number and its frequency in map, add number to freq[frequency]
4. initialise empty result list
5. loop from largest possible frequency down to 1
    * for each number in frequency add to results list
    * once result contains k numbers return it

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res