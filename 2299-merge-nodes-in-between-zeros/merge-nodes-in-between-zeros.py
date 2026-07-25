class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        curr=head.next
        s=0
        while curr:
            if curr.val==0:
                ans.append(s)
                s=0
            else:
                s+=curr.val
            curr=curr.next
        dumb=ListNode(0)
        cur=dumb
        for x in ans:
            cur.next=ListNode(x)
            cur=cur.next
        return dumb.next