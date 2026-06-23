class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # checking for a permutation essentially means that 
        # there is some substring in s2 that has the same frequency count as s1

        if len(s1) > len(s2):
            return False

        # we can check windows of size len(s1)
        left, right = 0, len(s1) - 1

        # use a list of size 26 to track frequencies
        s1_counts = [0] * 26
        for s in s1:
            s1_counts[ord(s) - 97] += 1 

        s2_counts = [0] * 26
        for i in range(right + 1):
            s2_counts[ord(s2[i]) - 97] += 1

        # check windows
        while right < len(s2):
            if s1_counts == s2_counts:
                return True
            
            # otherwise shift window down

            s2_counts[ord(s2[left]) - 97] -= 1
            left += 1

            right += 1
            if right < len(s2):
                s2_counts[ord(s2[right]) - 97] += 1
        
        # if we've gone through all possible windows, then there are no permutations
        return False
