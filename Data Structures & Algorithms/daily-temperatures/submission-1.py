class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # [30, 38, 30, 36, 35, 40, 28]
        # res = [0]*len(temperatures)

        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = j-i
        #             break
        #         continue
        
        # return res

        res = [0] * len(temperatures)

        stack = []      # stores indices

        for i in range(len(temperatures)):

            # Current temperature is warmer
            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev = stack.pop()

                res[prev] = i - prev

            stack.append(i)

        return res
