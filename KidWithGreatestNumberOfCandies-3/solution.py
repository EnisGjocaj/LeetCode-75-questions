#AD HOC solution

class Solution(object):
    def kidWithMaxCandies(self, candies, extraCandies):
        result = []

        maxCandies = max(candies)

        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)

        return result


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    result = solution.kidWithMaxCandies(candies, extraCandies)
    print(f"Test Case 1: {result}")  # Expected output: [True, True, True, False, True]

    # Test Case 2
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    result = solution.kidWithMaxCandies(candies, extraCandies)
    print(f"Test Case 2: {result}")  # Expected output: [True, False, False, False, False]

    # Test Case 3
    candies = [12, 1, 12]
    extraCandies = 10
    result = solution.kidWithMaxCandies(candies, extraCandies)
    print(f"Test Case 3: {result}")  # Expected output: [True, False, True]


# Complexity Analysis


# Here, n is the number of kids.

# Time complexity: O(n)

# We iterate over the candies array to find out maxCandies which takes O(n) time.
# We iterate over the candies array once more. We check for each kid whether they will have the most candies among all the children after receiving extraCandies and push the result in result which takes O(1) time. It requires O(n) time for n kids.


# Space complexity: O(1)

# Without counting the space of input and output, we are not using any space except for some integers like maxCandies and candy.