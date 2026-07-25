class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums) - 1)
        return nums


    def sort(self, arr, left, right):
        if left >= right:
            return
        
        mid = left + ((right - left) // 2)
        self.sort(arr, left, mid)
        self.sort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)


    def merge(self, arr, left, mid, right):
        i = left
        j = mid + 1

        merged = []
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1
        
        while i <= mid:
            merged.append(arr[i])
            i += 1
        
        while j <= right:
            merged.append(arr[j])
            j += 1
        

        for i in range(left, right + 1):
            arr[i] = merged[i - left]
        

        