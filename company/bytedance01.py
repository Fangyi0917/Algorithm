
def goodEditor(str):
        i = 0
        while i + 3 <= len(str):
                while i >= 0 and isWrong1(str[i:i+3]):
                        str = str[:i+1] + str[i+2:]
                        i -= 1
                if(i+4 <= len(str)):
                        while i >= 0 and isWrong2(str[i:i+4]):
                                str = str[:i+2]+str[i+3:]
                                i -= 1

                i += 1
        return str


def isWrong1(str):
        if str[0] == str[1] and str[1] == str[2]:
                return True
        else:
                return False

def isWrong2(str):
        if str[0] == str[1] and str[2] == str[3] and str[1] != str[2]:
                return True
        else:
                return False

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        str2 = input()
        print(goodEditor(str2))