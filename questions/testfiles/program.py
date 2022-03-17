# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root) :
    # write your code here
    return helper(root.left, root.right)
    
def helper(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return helper(left.left, right.right) and helper(left.right, right.left)