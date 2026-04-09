class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
            if len(nums) <= 1:
                return nums
            length = len(nums)
            half = length//2
            left= self.sortArray(nums[:half])
            right = self.sortArray(nums[half:])
            return mergeSort(left, right)



def mergeSort(left, right):
    i=0
    j=0
    arr=[]
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    while i<len(left):
        arr.append(left[i])
        i+=1
    
    while j<len(right):
        arr.append(right[j])
        j+=1
    return arr
        