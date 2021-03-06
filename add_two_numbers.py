"""
Ques. Add Two Numbers
T.C. = O(n)
S.C. = O(n)
Link - https://leetcode.com/problems/add-two-numbers/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0) 
        cur = head 
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            digit = carry 
            
            if(l1 != None):
                digit += l1.val 
                l1 = l1.next 
            
            if(l2 != None):
                digit += l2.val
                l2 = l2.next
            
            if(digit > 9):
                carry =  1
                digit = digit % 10 
            else:
                carry = 0
            
            cur.next = ListNode(digit)
            cur = cur.next 
            
        return head.next
