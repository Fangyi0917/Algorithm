#深度优先搜索
#将火柴分为总长度相等的四组，每根火柴属于其中一组
def makesquare(nums):
    if not nums:
        return False
    L = len(nums)
    sidesum = sum(nums)
    sidelength = sidesum // 4
    if sidelength * 4 != sidesum:
        return False
    nums.sort(reverse=True)
    sums = [0 for i in range(4)]
    def dfs(index):
        if index == L:
            return sums[0] == sums[1] == sums[2] == sidelength
        for i in range(4):
            if sums[i] + nums[index] <= sidelength:
                sums[i] += nums[index]
                if dfs(index+1):
                    return True
                sums[i] -= nums[index]
        return False
    return dfs(0)
nums = [1,1,2,2,2,1]
print(makesquare(nums))


