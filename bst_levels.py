"""The genesis of this one is a codewars kata that asked for a tree traversal by levels.
The solution uses a queue and a list to house results as it steps through each node.

Normally these traversals are something like in order, post order, or pre order traversal, 
so this queue system could be adopted to tally up items by levels.
"""


class Node:
    def __init__(self, left, right, value=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return f"{value} {left} {right}"


a = Node(
    left=Node(
        left=None,
        right=Node(
            left=None,
            right=None,
            value=4),
        value=2),
    right=Node(
        left=Node(
            left=None,
            right=None,
            value=5),
        right=Node(
            left=None,
            right=None,
            value=6),

        value=3),
    value=1
)


def tree_by_levels(root):
    results = []

    if root is None:
        return results

    queue = [root]

    while queue:
        results.append(queue[0].value)
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return results

res = tree_by_levels(a)
print(res)
