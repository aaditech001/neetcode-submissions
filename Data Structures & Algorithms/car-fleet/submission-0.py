class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed together
        cars = list(zip(position, speed))

        # Sort by position in descending order
        cars.sort(reverse=True)

        stack = []

        # Process each car
        for pos, spd in cars:

            # Time needed to reach destination
            time = (target - pos) / spd

            stack.append(time)

            # If current car catches fleet ahead, merge them
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        