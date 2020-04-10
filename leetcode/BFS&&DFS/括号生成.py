#括号有效的判断
def valid(seq):
    val = 0
    for c in seq:
        if c == "(":
            val += 1
        else:
            val -= 1
        if val < 0:
            return False
    return val == 0

#回溯法
def generateparenthesis(n):
    ans = []
    def backtrack(s, left, right):
        if len(s) == 2*n:
            ans.append(''.join(s))
            s = []
            return
        if left < n:
            s.append('(')
            backtrack(s, left+1, right)
            s.pop()

        if right < left:
            s.append(')')
            backtrack(s, left, right+1)
            s.pop()
    backtrack([], 0, 0)
    return ans
    
#dfs
def generateparenthesis_dfs(n):
    ans = []
    def dfs(cur_s, left, right):
        if left == 0 and right == 0:
            ans.append(cur_s)
            return
        if right < left:
            return
        if left > 0:
            dfs(cur_s+'(', left -1, right)
        if left < right:
            dfs(cur_s+')', left, right-1)
    dfs("", n, n)
    return ans


n = 3      
print(generateparenthesis(n))


