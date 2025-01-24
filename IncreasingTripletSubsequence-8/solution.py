class Solution(object):

    def findTriplets(self, nums:[List]) -> bool:

        first = float("inf")
        second = float("inf")

        for n in nums:

            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False