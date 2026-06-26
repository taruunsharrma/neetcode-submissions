class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}      # Stores frequency of each character in the current window
        res = 0         # Stores the maximum valid window length found so far

        l = 0           # Left pointer of the sliding window

        # Expand the window one character at a time
        for r in range(len(s)):

            # Include the current character in the window
            count[s[r]] = 1 + count.get(s[r], 0)
            print(count)

            # If more than k characters must be replaced,
            # the window is no longer valid.
            #
            # Window size = (r - l + 1)
            # max(count.values()) = frequency of the most common character
            #
            # Characters needing replacement =
            # window size - most frequent character count
            while (r - l + 1) - max(count.values()) > k:

                # Remove the leftmost character from the window
                count[s[l]] -= 1

                # Move the left boundary to shrink the window
                l += 1

            # Current window is valid, update the answer
            res = max(res, r - l + 1)

        return res