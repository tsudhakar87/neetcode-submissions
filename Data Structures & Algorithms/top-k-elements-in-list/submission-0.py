from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive solution 

        return [num for num, val in Counter(nums).most_common(k)]

