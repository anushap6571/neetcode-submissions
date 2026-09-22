class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')', '{':'}', '[':']' }
        stack = []
        if len(s) < 2:
            return False

        for string in s:
            if string in hashmap:
                stack.append(string)
            else:
                if not stack:
                    return False

                top = stack[-1]

                if hashmap[top] == string:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
