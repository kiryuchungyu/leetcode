#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_num = self.stack[0]
        for i in range(len(self.stack)):
            if i != 0:
                if self.stack[i] < min_num:
                    min_num = self.stack[i]                
                    
        return min_num


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

"""
Accepted
31/31 cases passed (4964 ms)
Your runtime beats 5.02 % of python3 submissions
Your memory usage beats 54.14 % of python3 submissions (18 MB)
"""