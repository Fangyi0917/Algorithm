class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def isSymmetric(root):
    return isMirror(root,root)
    def isMirror(t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left) and t1.val == t2.val
            
    
