class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dire = path.split("/")
        for dir in dire:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if stack :
                    stack.pop()
            else:
                stack.append(dir)
        return "/" + "/".join(stack)
        