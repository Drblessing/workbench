class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Calculate the final state of the asteroids after all collisions.
        We calculate the end state after every new asteroid is added to the stack.
        The end state is not path dependent, so we can calculate it incrementally."""
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0:
                    # If the last asteroid is smaller, it is destroyed.
                    if stack[-1] < -a:
                        stack.pop()
                    # If the last asteroid is equal, both are destroyed.
                    elif stack[-1] == -a:
                        stack.pop()
                        break
                    # If the last asteroid is larger, the new asteroid is destroyed.
                    else:
                        break
                else:
                    stack.append(a)
        return stack
