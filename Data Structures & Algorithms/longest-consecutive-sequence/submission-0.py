class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)

        max_len = 0

        for num in nums:
            # this is the start of a sequence
            if num - 1 not in nums_set:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)

        return max_len
