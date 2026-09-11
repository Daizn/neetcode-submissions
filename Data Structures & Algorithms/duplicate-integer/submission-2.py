class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theset = set()
        for i in nums:
            if i in theset:
                return True
            theset.add(i)
        return False
