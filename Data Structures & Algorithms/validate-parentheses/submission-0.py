class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={")":"(","}":"{","]":"["}
        stack=[]
        for ch in s:
            if ch in hash_map:
                if stack and stack[-1]==hash_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
        