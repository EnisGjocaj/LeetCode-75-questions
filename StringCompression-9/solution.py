
class Solution(object):
    def stringCompression(self, chars: Link[str]) -> int:

        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while(i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            
            i += group_length
        return res


# Let n be the length of chars.

# Time complexity: O(n).

# All cells are initially white. We will repaint each white cell blue, and we may repaint some blue cells green. Thus each cell will be repainted at most twice. Since there are n cells, the total number of repaintings is O(n).

# Space complexity: O(1).

# We store only a few integer variables and the string representation of groupLength which takes up O(1) space.