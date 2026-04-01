class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        state = True if len(set(nums)) < len(nums) else False

        return state