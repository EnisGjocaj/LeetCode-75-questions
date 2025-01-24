
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero, i = 0, 0  # Initialize pointers
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                # Swap non-zero element with the element at the `nonzero` pointer
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1  # Move `nonzero` pointer
            i += 1  # Move `i` pointer



# Time complexity: O(n)
# We traverse the array once, and swaps take constant time.
# Space complexity: O(1)
# The solution is in-place, requiring no extra space.