class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def insert_level_order(self, arr, root, i, n):
        if i < n:
            if arr[i] == None:
                return
            temp = TreeNode(arr[i])
            root = temp

            # insert left child
            root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)

            # insert right child
            root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
        return root

