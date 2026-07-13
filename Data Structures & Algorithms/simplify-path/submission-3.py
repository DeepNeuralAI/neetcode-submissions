class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        stack = []

        for s in split_path:
            if not s or s == '.':
                continue
            
            if s == '..':
                if stack: stack.pop()
            else:
                stack.append(s)
        
        return '/' + '/'.join(stack)
            


        