#Dont iterate
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n!=0:
            del nums1[-n:]
            nums1 += nums2
            nums1.sort()

#iterate
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i, v in enumerate(nums2):
            nums1[i-n] = v
        nums1.sort()
        
