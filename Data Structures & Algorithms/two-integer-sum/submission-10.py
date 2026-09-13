class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            b = nums[i]
            for j in range(len(nums)):
                c = nums[j]
                a = b + c 
                if i != j and a == target:
                    return [i, j]
        return False