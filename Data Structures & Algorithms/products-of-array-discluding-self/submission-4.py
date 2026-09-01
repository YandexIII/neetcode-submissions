class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for i in range(1, len(nums)):
            result.append(nums[i - 1] * result[i-1])
            
        suffix = [1]
        for i in range(1, len(nums)):
            suffix.append(nums[-i] * suffix[i -1])

        for i in range(len(nums)):
            result[i] *= suffix[-(i+1)]

        return result



        