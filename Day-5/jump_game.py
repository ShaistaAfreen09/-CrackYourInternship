# the question states that we need to find the reaach last using the maximum jump in the array at posiitons.
#Approach : we can solve in way where if we supppose that stones are there  and numbers are written on it we need to jump and reach last stone using numbers so we ccan count how many steps are further required on reaching the other stone , if first is the last stone number then return not possible and if not then further stone valuei s greater than te steps needed than add it to steps and perform operation followed by reducing the jump and reaching the last stop.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stone = 0
        for n in nums:
            if stone<0:
                return False
            elif n >stone:
                stone = n
            stone -= 1
        return True