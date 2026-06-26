class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Pair each car's position with its speed.
        # Example:
        # position = [10, 8, 0]
        # speed    = [ 2, 4, 1]
        # pair = [(10,2), (8,4), (0,1)]
        pair = [[p, s] for p, s in zip(position, speed)]

        # Stack stores the ARRIVAL TIME of each fleet.
        #
        # We are NOT storing cars.
        # We are storing the time each fleet reaches the target.
        stack = []

        # Sort cars by position in ascending order and traverse in reverse.
        #
        # Why?
        # Because a car can only interact with cars in front of it.
        # So we process from the car closest to the destination
        # toward the farthest one.
        for p, s in sorted(pair)[::-1]:

            # Time required for this car to reach the target.
            time = (target - p) / s

            # Assume this car starts as its own fleet.
            stack.append(time)

            # Compare with the fleet directly ahead.
            #
            # stack[-1] -> current car's arrival time
            # stack[-2] -> fleet ahead's arrival time
            #
            # If current car reaches earlier (or at the same time),
            # it MUST catch the fleet ahead before or exactly at
            # the destination.
            #
            # Therefore, it is NOT a new fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # Every remaining arrival time in the stack
        # represents one unique fleet.
        return len(stack)