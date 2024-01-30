class Solution:
    def twoSum(self, nums, target):
        complement_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in complement_dict:
                return [complement_dict[complement], i]
            
            complement_dict[num] = i
        
        return []
nums1 = [2, 7, 11, 15]
target1 = 9
sol = Solution()
print(sol.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(sol.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(sol.twoSum(nums3, target3))  
        
