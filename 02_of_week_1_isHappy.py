"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True


#     3


# I am working on an easy math question Happy number Happy Number - LeetCode

# Happy Number
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation: 
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1
# My solutions

# Solution 1, 28ms 12.1mb

# string operations
# class Solution1:
#     def isHappy(self, n):
#         s = set()
#         while n != 1:
#             if n in s: return False
#             s.add(n)
#             n = sum([int(i) ** 2 for i in str(n)])
#         else:
#             return True
# Solution 2, 24ms, 12.3mb
# class Solution2:
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         s = set()
#         while n != 1:
#             if n in s: return False
#             s.add(n)

#             _sum = 0
#             while n:
#                 _sum += (n % 10) ** 2
#                 n //= 10
#             n = _sum

#         return n == 1
# Solution 3 the save as solution 2 minor changes (24ms, 12.3mb)
# class Solution3:
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         s = set()
#         while n:
#             if 1 in s:
#                 return True
#             if n in s:
#                 return False
#             s.add(n)
#             _sum = 0
#             while n:
#                 _sum += (n%10)**2 #leave unit digit
#                 n //= 10 #remvoe unit digit 
#             n = _sum
# Solution 4 without extra space(24ms, 12.3mb)
# class Solution4:
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         while n != 1 and n != 4:
#             _sum = 0
#             while n :
#                 _sum += (n % 10) * (n % 10)
#                 n //= 10
#             n = _sum

#         return n == 1
# TestCase

# class MyCase(unittest.TestCase):
#     def setUp(self):
#         self.solution = Solution3()

#     def test_1(self):
#         n = 19
#         check = self.solution.isHappy(n)
#         self.assertTrue(check)
# It's interesting that the last 3 solutions shared the same performance, though try best possibility to improve it.

# python performance programming-challenge comparative-review
# shareimprove this questionfollow
# edited Apr 4 '19 at 14:38

# 200_success
# 139k2121 gold badges179179 silver badges452452 bronze badges
# asked Apr 4 '19 at 11:24

# Alice
# 58311 silver badge88 bronze badges
# 1
# In general, you should never be using a benchmark that takes less than a second. Timings below that are way too variable. – Oscar Smith Apr 4 '19 at 18:29
# add a comment
# 1 Answer
# Active
# Oldest
# Votes

# 2

# Solution #2:

# class Solution2:
#     def isHappy(self, n):
#         # ...
#         while n != 1:
#             if n in s: return False
#             # ...

#     return n == 1
# You are looping while n != 1, without any break statements. There is no need to test n == 1 at the return statement at the end. Just return True.

# Solution #3 returns None if 0 is given as input, instead of returning True or False.

# Solution #4 becomes an endless loop if 0 is given as input.

# Are there any other stopping conditions other that n == 0, n == 1 or n == 4? It isn't clear that all unhappy numbers result in a loop containing the value 4, so the validity of this approach is in question.

# Update: Actually Wikipedia provides a clear argument that unhappy numbers will arrive in a loop containing the value 4, so this approach is valid, but should included a comment with a link to that proof.

# In all your solutions, your loop is testing at least two conditions, such as both n != 1 and n is s. Why not initialize s to contain a 1 (or even just leave it as an empty set), and then only test n in s. No special cases.

# def is_happy(n):
#     s = { 1 }

#     while n not in s:
#         s.add(n)
#         n = sum(i * i for i in map(int, str(n)))

#     return n == 1
# Update:

# Since Wikipedea has proof that all positive unhappy numbers end in the sequence 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ..., and happy numbers end in the sequence 1 → 1 → ..., you can create a set of these termination values (including 0 → 0 → ...), and no longer needed to maintain the set of "seen" values. By using all numbers in the unhappy loop, we can terminate the search up to 8 iterations earlier over just checking for n == 1 and n == 4.

# def is_happy(num):
#     # See https://en.wikipedia.org/wiki/Happy_number#Sequence_behavior
#     terminal = { 0, 1, 4, 16, 20, 37, 42, 58, 89, 145 }

#     while num not in terminal:
#         num = sum(i * i for i in map(int, str(num)))

#     return n == 1