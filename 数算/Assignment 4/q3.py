def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    pointerA, pointerB = headA, headB

    while pointerA is not pointerB:
        pointerA = headB if pointerA is None else pointerA.next
        pointerB = headA if pointerB is None else pointerB.next

    return pointerA

