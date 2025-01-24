#Solution approach using suffix and prefix arrays


class Solution(object):
    def productOfArrayExceptSelf(self, nums):

        n = len(nums)

        ans = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        
        return ans

        

# Complexity


# Time complexity:

# O(n)
# We make two passes through the array, once for computing prefix products and once for suffix products.

# Space complexity:

# O(n) (excluding the result array).
# The solution uses constant space for the running suffix product.