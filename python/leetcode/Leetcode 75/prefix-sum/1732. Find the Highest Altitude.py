class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """Calculate the max of a running sum."""

        m_alt = cur_alt = 0
        for change in gain:
            cur_alt += change
            m_alt = max(m_alt, cur_alt)

        return m_alt
