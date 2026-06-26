class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Brute Force
        # Get the ord of charc from s1 and use sliding window based on leng
        # and match the ord if matches then true or else false
        # another thing we can compare the keys

        # s1 = "".join(sorted(s1))

        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         substring = s2[i: j+1]
        #         substring = "".join(sorted(substring))

        #         if len(s1) != len(substring):
        #             continue

        #         if s1 == substring:
        #             return True
        
        # return False


        # Sliding Window
        if len(s1) > len(s2):
            return False
        
        s1Count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == s1Count:
            return True
    
        l = 0

        for r in range(len(s1), len(s2)):

            # Add new character
            window[s2[r]] += 1

            # Remove left character
            window[s2[l]] -= 1

            print(window)
            # if window[s2[l]] == 0:
            #     del window[s2[l]]

            l += 1

            if window == s1Count:
                return True

        return False


