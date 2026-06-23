class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        char_map = {}

        while right < len(s):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)

            char_map[s[right]] = right

            right += 1
            max_length = max(max_length, right - left)
            

        return max_length



