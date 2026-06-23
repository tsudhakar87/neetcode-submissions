class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # O(n) time where n is len(s)
        # O(m) space where m is the # of unique chars in s and t

        if len(t) > len(s):
            return ""
        
        if s == t:
            return t

        result = s

        # make a frequency map for chars in t
        # we can use this to evaluate substrings in s
        t_freq = {}
        s_freq = {}

        for letter in t:
            t_freq[letter] = t_freq.get(letter, 0) + 1
            s_freq[letter] = 0
        

        # sliding window

        left, right = 0, 0
        need = len(t_freq)
        have = 0
        foundValidWindow = False

        while right < len(s):
            # print("left:", left, "right:", right, "s[left:right+1]:", s[left:right+1], "have:", have)
            if s[right] in t_freq:
                s_freq[s[right]] += 1
                if s_freq[s[right]] == t_freq[s[right]]:
                    have += 1
            
            while have == need:
                foundValidWindow = True
                # check if current valid window is shorter than what we have so far
                if right - left + 1 < len(result):
                    result = s[left : right + 1]

                if s[left] in s_freq:
                    s_freq[s[left]] -= 1

                if s[left] in t_freq and s_freq[s[left]] < t_freq[s[left]]:
                    have -= 1

                left += 1
            
            right += 1
        # print("left:", left, "right:", right, "s[left:right+1]:", s[left:right+1], "have:", have)
        
        if foundValidWindow:
            return result
        else:
            return ""