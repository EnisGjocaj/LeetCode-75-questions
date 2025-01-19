#

class Solution(object):
    def reverseVowels(self, s):

        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"

        while start < end:

            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            while start < end and vowels.find(word[start]) == -1:
                end -= 1
            
            word[start], word[end] = word[end], word[start]

            start +=1
            end -= 1
        
        return "".join(word)



if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    s1 = "hello"
    result1 = solution.reverseVowels(s1)
    print(f"Test Case 1 - Reverse vowels of '{s1}': {result1}")

    # Example 2:
    s2 = "leetcode"
    result2 = solution.reverseVowels(s2)
    print(f"Test Case 2 - Reverse vowels of '{s2}': {result2}")

    # Example 3:
    s3 = "aA"
    result3 = solution.reverseVowels(s3)
    print(f"Test Case 3 - Reverse vowels of '{s3}': {result3}")

    # Example 4 (Edge case with no vowels):
    s4 = "bcdf"
    result4 = solution.reverseVowels(s4)
    print(f"Test Case 4 - Reverse vowels of '{s4}': {result4}")

    # Example 5 (Edge case with all vowels):
    s5 = "aeiou"
    result5 = solution.reverseVowels(s5)
    print(f"Test Case 5 - Reverse vowels of '{s5}': {result5}")