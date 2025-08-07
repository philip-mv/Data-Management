keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printCombination(combination,curr,output,n):
    if(curr == n):
        print(*output,sep=",")
        return
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        printCombination(combination,curr+1,output,n)
        output.pop()
        if(combination[curr]== 0 or combination[curr]== 1):
            return
combination = [6,8,7]
n = len(combination)
printCombination(combination,0,[],n)