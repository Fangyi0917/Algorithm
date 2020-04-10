#当前颜色起始下标为i，下一个颜色起始下标为j，则需要的球个数need = 3-（j-i）
#如何解决连续碰撞的问题，在循环中，计算need时判断是否<0
# 如果need小于0则说明上一次碰撞以后连续球>=3，那么继续dfs减去i-j的新board
import collections
def findMinStep(board,hand):
    def dfs(board,hand):
        if not board:
            return 0
        res = float("inf")
        i = 0
        while i<len(board):
            j=i+1
            while j<len(board) and board[i]==board[j]:
                j+=1
            need = 3-(j-i)
            if hand[board[i]]>=need:
                need = max(0,need) #为了解决已经有的连接的球，并且球数可能大于3个
                hand[board[i]]-=need
                temp = dfs(board[:i]+board[j:],hand)
                if temp>=0:
                    res = min(res,need+temp)
                hand[board[i]]+=need
            i=j
        return res if res!=float('inf') else -1
    return dfs(board,collections.Counter(hand))

board = "WWRRBBWW"
hand = "WRBRW"
print(findMinStep(board, hand))
