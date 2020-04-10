
#回溯法
def letterCombinations(digits):
    ans = []
    letters =  {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
    def backtrace(combination, cur_digits):
        if len(combination) == len(digits):
            ans.append(combination)
            return 
        else:
            for c in letters[cur_digits[0]]:
                backtrace(combination+c, cur_digits[1:])
    backtrace("", digits)
    return ans

digits = "32"
print(letterCombinations(digits))