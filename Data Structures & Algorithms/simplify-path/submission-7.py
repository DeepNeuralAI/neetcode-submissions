class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')

        stack = []
        for s in paths:
            if s == '..':
                if stack: stack.pop()
            elif s != '' and s != '.':
                stack.append(s)
        
        return '/' + '/'.join(stack) 

        