class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Define Search Space
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        total = n + m
        half = (total + 1) // 2

        l = max(0, half - m)
        r = min(half, n)
        

        while l <= r:
            left = (l + r) // 2
            right = half - left
            
            res = self.isValid(nums1, nums2, left, right)

            if res == 0:
                l1 = left - 1
                l2 = right - 1
                
                leftMax = max(nums1[l1] if l1 >= 0 else float('-inf'), 
                              nums2[l2] if l2 >= 0 else float('-inf'))
                
                if total % 2 == 1:
                    return float(leftMax)
                
                rightMin = min(nums1[left] if left < n else float('inf'), 
                               nums2[right] if right < m else float('inf'))
                
                return (leftMax + rightMin) / 2.0
            elif res == 1:
                r = left - 1
            else:
                l = left + 1
        

    def isValid(self, nums1, nums2, left, right):
        l1 = left - 1
        r1 = left

        l2 = right - 1
        r2 = right

        n1 = nums1[l1] if l1 >= 0 else float('-inf')
        m1 = nums1[r1] if r1 < len(nums1) else float('inf')

        n2 = nums2[l2] if l2 >= 0 else float('-inf')
        m2 = nums2[r2] if r2 < len(nums2) else float('inf')

        if n1 <= m2 and n2 <= m1:
            return 0
        
        if n1 > m2:
            return 1
        
        else:
            return -1
