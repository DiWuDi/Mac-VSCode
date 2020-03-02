# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

# class SLinkedList:
#     def __init__(self):
#         self.head = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode,
        :typ l2: ListNode,
        :rtype: ListNode:
        """
        curr = dummy = ListNode(0)
        #print (curr.val)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
            
        curr.next =l1 or l2
        
        return dummy.next


l1 = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(4)
l1.next = e2
e2.next = e3
e3.next = None

l2 = ListNode(1)
d2 = ListNode(3)
d3 = ListNode(4)
l2.next = d2
d2.next = d3
d3.next = None


test = Solution()
result = test.mergeTwoLists(l1,l2)
while result:
    print (result.val)
    result = result.next



# e1 = ListNode(1)
# e2 = ListNode(2)
# e3 = ListNode(4)
# e1.next = e2
# e2.next = e3
# e3.next = None
# l1 = SLinkedList()
# l1.head = e1


# d1 = ListNode(1)
# d2 = ListNode(3)
# d3 = ListNode(4)
# d1.next = d2
# d2.next = d3
# d3.next = None
# l2 = SLinkedList()
# l2.head = d1
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4