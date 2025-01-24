
class Solution(object):
    def reverseWord(self,s: str) -> str:
        return ' '.join(reversed(s.split()))


if __name__ == "__main__":
    solution = Solution()

    s1 = "hello this is me"
    result1 = solution.reverseWord(s1)
    print(f"Test Case 1 - Reverse word of '{s1}': {result1}")