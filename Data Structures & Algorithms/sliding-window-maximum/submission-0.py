class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []
        n = len(nums)

        l = r = 0
        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r >= k - 1:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return output
