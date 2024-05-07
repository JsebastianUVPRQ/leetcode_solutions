# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):        
    def addTwoNumbers(self, l1, l2):
        '''
        Time complexity: O(max(m, n))
        '''
        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

class Solution_3:
    def countEqualRows(self, grid):
        '''
        Time complexity: O(n^2)
        '''
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == grid[j]:
                    count += 1
        return count
    def Equalroewcount(self, grid):
        '''
        Time complexity: O(n)
        '''
        n = len(grid)
        count = 0
        rows = {}
        for i in range(n):
            if tuple(grid[i]) in rows:
                count += rows[tuple(grid[i])]
                rows[tuple(grid[i])] += 1
            else:
                rows[tuple(grid[i])] = 1
        return count
   
