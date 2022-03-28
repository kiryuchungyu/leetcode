#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from curses.ascii import SO
from unicodedata import digit


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_ = 0
        for i_ in range(len(digits)):
            i_power = len(digits) - i_ - 1
            power = 10 ** i_power
            sum_ += digits[i_] * power
        num = sum_ + 1
        output_list = [int(str_) for str_ in str(num)]
        return output_list

# @lc code=end
"""
Accepted
111/111 cases passed (36 ms)
Your runtime beats 83.16 % of python3 submissions
Your memory usage beats 14.75 % of python3 submissions (14.4 MB)
"""