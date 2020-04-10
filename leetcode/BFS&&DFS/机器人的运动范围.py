from queue import Queue
def calsum(x,y):
    sum = 0
    sxy = str(x) + str(y)
    for c in sxy:
        sum += int(c)
    return sum
def movingCount_bfs(m,n,k):
    q = Queue()
    q.put((0, 0))
    s = set()
    while not q.empty():
        x, y = q.get()
        if (x, y) not in s and 0 <= x < m and 0 <= y < n and calsum(x,y) <= k:
            s.add((x, y))
            for nx, ny in [(x + 1, y), (x, y + 1)]:
                q.put((nx, ny))
    return len(s)


def movingCount_rule(m,n,k):
    vis = set()
    vis.add((0,0))
    for i in range(m):
        for j in range(n):
            if ((i-1,j) in vis or (i ,j-1) in vis) and calsum(i,j) <= k:
                vis.add((i,j))
    return len(vis)

def movingCount_dfs(m,n,k):
    def dfs(i,j):
        if not 0 <= i < m or not 0 <= j < n or k < calsum(i,j) or (i,j) in visited:
            return 0
        visited.add((i,j))
        return 1+ dfs(i+1, j) + dfs(i,j+1)
    visited = set()
    return dfs(0,0)




m = 2
n = 3
k = 1

print(movingCount_dfs(m,n,k))
