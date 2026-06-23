from collections import defaultdict, Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find the longest window with length m, with at most k characters that are
        # not the same as the other m - k characters, which should all be the same letter

        if len(s) <= 1:
            return len(s)

        left, right = 0, 0
        maxLen = 0
        maxFreq = 0
        numReplacements = 0
        counts = defaultdict(int)

        while right < len(s):
            counts[s[right]] += 1
            maxFreq = max(maxFreq, counts[s[right]])

            numReplacements = (right - left + 1) - maxFreq

            if numReplacements > k:
                counts[s[left]] -= 1
                left += 1

            if right - left + 1 > maxLen:
                maxLen = right - left + 1

            right += 1
        
        return maxLen
            

