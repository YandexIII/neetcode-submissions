class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max = 0
        for i in set_nums:
            if i -1 not in set_nums:
                j = i
                temp = 1
                while j +1 in set_nums:
                    temp += 1
                    j += 1
                if temp > max:
                    max = temp
        
        return max