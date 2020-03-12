#超时，通过20%
def numOfcase(n,maxd,case):
        casesum = 0
        for i in range(n-2):
                casenum = 0
                # if case[-1] - case[i] <= maxd:
                #         casesum += (n-i)*(n-i-1)*(n-i-2)//6%99997867
                # else:
                j = i + 1
                while j < n and (case[j] - case[i] <= maxd):
                        casenum += 1
                        j += 1
                if casenum >= 2:
                        casesum += casenum * (casenum-1) %99997867// 2 
        return casesum

if __name__ == "__main__":
        n,maxd = map(int, input().split())
        case = list(map(int, input().split()))
        print(numOfcase(n,maxd,case))
                        
                