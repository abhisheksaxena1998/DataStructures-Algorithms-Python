# https://leetcode.com/problems/jump-game/submissions/
# T.C O(n)
# greedy 
class Solution:
    def canJump(self, nums) :
        lastpos = len(nums)-1
        for i in range(lastpos,-1,-1):
            if i+nums[i]>=lastpos:
                lastpos = i
        return lastpos == 0
obj=Solution()
print(obj.canJump())
