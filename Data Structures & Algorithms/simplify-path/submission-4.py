class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []

        for cur in paths:
            if cur == '..':
                if stack: stack.pop()
            elif cur == '.' or not cur:
                continue
            else:
                stack.append(cur)
        
        return '/' + '/'.join(stack)
            


        