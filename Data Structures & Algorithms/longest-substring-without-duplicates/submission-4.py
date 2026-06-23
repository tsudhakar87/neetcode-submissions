class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) <= 1:
        #     return len(s)

        # seen = set()

        # left, right = 0, 0
        # max_length = 0

        # while right < len(s):
        #     # print("left:", left, "-- right:", right, "-- s[left]:", s[left], "-- s[right]:", s[right], "-- seen: ", seen, "-- max length:", max_length)
        #     if s[right] in seen:
        #         while s[left] in seen:
        #             seen.remove(s[left])
        #             left += 1
        #     else:
        #         seen.add(s[right])
        #         max_length = max(max_length, right - left)
            
        #     right += 1
            

        # # print("left:", left, "right:", right, "max length:", max_length)

        # return max(max_length, right - left)


        left, right, max_length = 0, 0, 0
        char_map = {}

        while right < len(s):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)

            char_map[s[right]] = right

            right += 1
            max_length = max(max_length, right - left)
            

        return max_length



