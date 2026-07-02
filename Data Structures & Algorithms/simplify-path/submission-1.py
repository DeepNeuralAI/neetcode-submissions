class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = path.split('/')
        
        
        for c in cur:
            if c == '..':
                if stack:
                    stack.pop()
            elif c == '.' or c == '':
                continue
            else:
                stack.append(c)
        
        s = '/'.join(stack)
        return '/' + s