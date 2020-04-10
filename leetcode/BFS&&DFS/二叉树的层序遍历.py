from queue import Queue
from collections import deque
def levelOrder(root):
    if not root:
            return []
    ans = []


    #回溯法
    def backtrace(node,level):
        if level == len(ans):
            ans.append([])
        ans[level].append(node.val)
        if node.left:
            backtrace(node.left,level+1)
        if node.right:
            backtrace(node.right,level+1)
    backtrace(root, 0)
    return ans


    #BFS
    def bfs(root):
        level = 0
        queue = deque([root,])
        while queue:
            ans.append([])
            queue_length = len(queue)
            for i in range(queue_length):
                node = queue.popleft()
                ans[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
    bfs(root)
    return ans
            


    
        
        


    
        