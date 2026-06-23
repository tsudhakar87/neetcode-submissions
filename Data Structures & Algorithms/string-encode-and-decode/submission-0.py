class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            length = len(string)

            encoded_str += str(length) + "#" + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0
        strs = []

        while right < len(s):
            if s[right] != "#":
                right += 1
            else:
                start = right + 1
                end = start + int(s[left:right])

                strs.append(s[start : end])

                left = right = end

        return strs
