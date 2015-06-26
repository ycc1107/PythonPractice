
MOVES = { 'knight':{
         0: [4, 6],
         1: [6, 8],
         2: [7, 9],
         3: [4, 8],
         4: [0, 3, 9],
         5: [],
         6: [0, 1, 7],
         7: [2, 6],
         8: [1, 3],
         9: [2, 4]
    },
         'bishop':{
        0:[7,9],
        1:[5,9],
        2:[4,6],
        3:[5,7],
        4:[2,8],
        5:[1,3,7,9],
        6:[2,8],
        7:[0,3,5],
        8:[4,6],
        9:[0,1,5]
                }
}


def getNumbers(initPosition, move, checkLst,curNumber):
    if len(curNumber) == 3:
        num = ''.join([str(i) for i in curNumber])
        checkLst.add(num)
        #print(checkLst)
    else:
        for nextPosition in move[initPosition]:
            
            curNumber.append(nextPosition)  
            #print(curNumber)
            getNumbers(nextPosition, move,checkLst,curNumber)
            curNumber.pop()
def main():
    res = set()
    move = MOVES['bishop']
    for i in range(2,10):
        getNumbers(i,move,res,[i])

    print(res)   
    print(len(res))



if __name__ == "__main__":main()
