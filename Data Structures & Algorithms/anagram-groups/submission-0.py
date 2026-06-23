from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force/naive solution

        # can use a map to group anagrams together
        anagrams = {}

        # need logic to figure out if a str is 
        # an anagram of any of the current keys in the map
        for string in strs:
            sorted_str = "".join(sorted(string))

            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]

        # then, return all the lists in the values of the map in one list

        result = [anagrams[key] for key in anagrams]

        return result