#First method: Two pointers

class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0

        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1
        
        return "".join(result)


if __name__ == "__main__":

    solution = Solution()

    # Test cases
    word1 = "abc"
    word2 = "pqr"
    result = solution.mergeAlternately(word1, word2)
    print("Merged result:", result)  



# Complexity Analysis


# Here, m is the length of word1 and n is the length of word2.

# Time complexity: O(m+n)

# We iterate over word1 and word2 once and push their letters into result. It would take O(m+n) time.

# Space complexity: O(1) or O(m+n)

# Without considering the space consumed by the input strings (word1 and word2) and the output string (result), we do not use more than constant space.