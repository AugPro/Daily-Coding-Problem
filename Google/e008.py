"""This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def unival(self):
        left = None if self.left is None else self.left.unival()
        right = None if self.right is None else self.right.unival()
        if left is None and right is None: return self.val
        if right==left==self.val:
            return self.val

    def unicount(self):
        left = 0 if self.left is None else self.left.unicount()
        right = 0 if self.right is None else self.right.unicount()
        return left + right + (self.unival() is not None)


if __name__ == '__main__':
    node = Node(0,
                Node(1),
                Node(0,
                    Node(1,
                        Node(1),
                        Node(1)
                        ),
                    Node(0)
                    )
                )
    assert node.unicount()==5, node.unicount()
