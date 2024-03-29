class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        char_index_map = {}  # To store the index of each character in the current substring
        max_length = 0
        start = 0

        for end in range(n):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1  # Move the start pointer to the next index of the repeating character

            char_index_map[s[end]] = end
            current_length = end - start + 1
            max_length = max(max_length, current_length)

        return max_length

# Example usage:
solution = Solution()

s1 = "abcabcbb"
print(solution.lengthOfLongestSubstring(s1))  # Output: 3

s2 = "bbbbb"
print(solution.lengthOfLongestSubstring(s2))  # Output: 1

s3 = "pwwkew"
print(solution.lengthOfLongestSubstring(s3))  # Output: 3
