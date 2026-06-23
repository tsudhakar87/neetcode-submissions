import heapq
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1 or k == 1:
            return nums

        left = 0
        right = k-1
        result = []

        max_heap = [(-num, idx) for idx, num in enumerate(nums[left : right + 1])]
        heapq.heapify(max_heap) # to get max

        while right < len(nums):
            curr_max = max_heap[0]
            
            while max_heap[0][1] < left:
                curr_max = heapq.heappop(max_heap)

            curr_max = max_heap[0]

            result.append(-curr_max[0])

            left += 1
            right += 1

            if right < len(nums):
                heapq.heappush(max_heap, (-nums[right], right))
            

        return result