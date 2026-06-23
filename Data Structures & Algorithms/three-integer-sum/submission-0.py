class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(target: int, start_idx: int) -> List[List[int]]:
            left = start_idx
            right = len(nums) - 1
            result = []

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([nums[left], nums[right], -target])
                    left += 1
                    right -= 1

            return result

        result = []
        # call two sum on each num's opposite
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res = twoSum(-nums[i], i + 1)

            if res:
                for l in res:
                    result.append(l)
        
        result = {tuple(sorted(r)) for r in result}
        result = list(list(r) for r in result)

        return result