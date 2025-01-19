#Single scan solution

class Solution(object):
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:

                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n

if __name__ == "__main__":
    solution = Solution()

    # Example test cases:
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    result1 = solution.canPlaceFlowers(flowerbed1, n1)
    print(f"Test Case 1 - Can place {n1} flowers? {result1}")
    print(f"Updated flowerbed: {flowerbed1}\n")

    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    result2 = solution.canPlaceFlowers(flowerbed2, n2)
    print(f"Test Case 2 - Can place {n2} flowers? {result2}")
    print(f"Updated flowerbed: {flowerbed2}\n")

    flowerbed3 = [0, 0, 0, 0, 0]
    n3 = 3
    result3 = solution.canPlaceFlowers(flowerbed3, n3)
    print(f"Test Case 3 - Can place {n3} flowers? {result3}")
    print(f"Updated flowerbed: {flowerbed3}\n")

    flowerbed4 = [1, 1, 1, 1, 1]
    n4 = 1
    result4 = solution.canPlaceFlowers(flowerbed4, n4)
    print(f"Test Case 4 - Can place {n4} flowers? {result4}")
    print(f"Updated flowerbed: {flowerbed4}\n")


# Time complexity: O(n). A single scan of the flowerbed array of size n is done.

# Space complexity: O(1). Constant extra space is used.