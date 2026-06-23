class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        chars = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        for char in s:
            if char in chars:
                stack.append(char)
            elif stack and char == chars[stack[-1]]:
                stack.pop()
            else:
                return False

        return not stack