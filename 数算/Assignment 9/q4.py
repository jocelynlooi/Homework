from collections import deque
import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(str(node.val))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def main():
    data = sys.stdin.read().strip().split()
    seen = set()
    root = None
    for tok in data:
        num = int(tok)
        if num in seen:
            continue
        seen.add(num)
        root = insert(root, num)

    out = ' '.join(level_order(root))
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
