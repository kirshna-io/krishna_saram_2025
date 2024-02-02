class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Initialize left and right arrays to store prefix and suffix products
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate prefix products
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        # Calculate suffix products
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        # Calculate the final result
        result = [left_products[i] * right_products[i] for i in range(n)]
        
        return result

# Example usage:
solution = Solution()

nums1 = [1, 2, 3, 4]
print(solution.productExceptSelf(nums1))  # Output: [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
print(solution.productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
