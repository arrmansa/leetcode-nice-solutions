class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums.sort(key=lambda n: n / (10**len(str(n))-1), reverse=True)
        return "".join(map(str, nums))
