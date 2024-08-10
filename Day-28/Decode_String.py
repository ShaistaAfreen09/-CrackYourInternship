class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c==']':
                char=""
                while stack and stack[-1]!='[':
                    char=stack.pop()+char

                # for removing '['

                stack.pop()
                number=""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number 
                stack.append(int(number)*char)
            else:
                stack.append(c)
        return "".join(stack)
        