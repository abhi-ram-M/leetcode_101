class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_e = None
        c = 0
        for i in nums:
            if c == 0:
                c = 1
                m_e = i
            else:
                if m_e == i:
                    c += 1
                else:
                    c -= 1
        return m_e

        