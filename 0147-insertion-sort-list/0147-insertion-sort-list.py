# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# understanding purpose only for below code
#def insertion_sort(arr):
    # Traverse through all elements in the list
    #for i in range(1, len(arr)):
       # key = arr[i]  # The current element to be inserted in the sorted portion
       # j = i - 1  # Pointer to the last element of the sorted portion

        # Move elements of arr[0..i-1], that are greater than key, one position ahead
       # while j >= 0 and arr[j] > key:
           # arr[j + 1] = arr[j]
            #j -= 1

        # Place the key at its correct position
        #arr[j + 1] = key

   # return arr
#Actual code is starting here

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        x=[]
        temp=head
        while temp!=None:
            x.append(temp.val)
            temp=temp.next
        x.sort()
        temp=head
        for i in x:
            temp.val=i
            temp=temp.next
        return head