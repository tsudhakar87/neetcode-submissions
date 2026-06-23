class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                total_product *= num

        result = []

        for num in nums:
            if num == 0:
                result.append(total_product)
            elif zero_count == 1:
                result.append(0)
            else:
                result.append(int(total_product / num))

        return result