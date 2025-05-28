class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

def josephus_circle(n, k):
    # 创建循环链表
    head = Node(1)
    current = head
    for i in range(2, n + 1):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    current.next = head

    result = []
    current = head
    prev = None

    while current.next != current:
        # 找到第k个节点
        for _ in range(k - 1):
            prev = current
            current = current.next
        # 杀掉第k个节点
        result.append(str(current.number))
        prev.next = current.next
        current = prev.next

    # 最后剩下的一个人
    #result.append(str(current.number))
    #return ' '.join(result[:-1])
    return ' '.join(result)


n, k = map(int, input().split())


print(josephus_circle(n, k))
