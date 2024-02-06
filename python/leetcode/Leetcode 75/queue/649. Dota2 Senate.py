from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """Predict the winning party based on the senate votes."""

        # Create two queues to store the indices
        radiant = deque()
        dire = deque()

        # Turn string into dequeues to make it fast
        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        # Iterate until one of the queue is empty
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            if r_idx < d_idx:
                radiant.append(r_idx + len(senate))
            else:
                dire.append(d_idx + len(senate))

        return "Radiant" if radiant else "Dire"


if "__main__" == __name__:
    s = Solution()
    print(s.predictPartyVictory("RDD"))
