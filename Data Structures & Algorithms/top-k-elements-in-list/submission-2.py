from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # easy naive solution ---

        # return [num for num, _ in Counter(nums).most_common(k)]

        # naive solution ---

        # counts = defaultdict(int)

        # for num in nums:
        #     if num in counts:
        #         counts[num] += 1
        #     else:
        #         counts[num] = 0

        # sorted_counts = sorted(counts.items(), key=lambda item: item[1])

        # result = []

        # for _ in range(k):
        #     val = sorted_counts.pop()
        #     result.append(val[0])

        # return result

        # bucket sort ---

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
