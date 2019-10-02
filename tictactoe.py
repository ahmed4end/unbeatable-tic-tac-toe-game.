import os
tic =[0,0,0,
      0,0,0,
      0,0,0]

def minimax(state, depth, player):#ِplayers:(Ai: +1 & human: -1) #best move selector function.
    best = [-1, -float("inf")] if player== +1 else [-1, +float("inf")] #<<human
    wins  =((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) #wins combinations
    empties = [i for i,j in enumerate(state) if j==0] #empty cells 
    win =lambda player: any(map(lambda w: state[w[0]]==state[w[1]]==state[w[2]]==player, wins))
    minimax.check = win #end slot.
    if depth == 0 or win(+1) or win(-1):
        evaluate = 1 if win(+1) else -1 if win(-1) else 0
        return [-1, evaluate]
    for cell in empties: 
        state[cell] = player
        score = minimax(state, depth - 1, -player) #recursion core
        state[cell] = 0
        score[0] = cell 
        if player == +1: best = score if score[1] > best[1] else best  #maximizing
        else:            best = score if score[1] < best[1] else best  #minimizing
    return best

############## user interface handling ##################

def pprint(tic): #printing function for simple view.
    result = []
    for i in range(0,9,3):
        piece  = str(tic[i:i+3]).replace(" 0", " ").replace("0", " ").replace(" -1","x").replace("-1","x").replace(" 1", "o").replace("1", "o").replace(",", " ")
        result.append(piece)
    print("\n".join(result))

pprint(tic)
while True:
    while True:
        tic[int(input("your turn (1-9): "))-1] = -1
        os.system("cls")
        pprint(tic) #print
        depth = len([i for i in tic if i == 0]) #human turn
        tic[minimax(tic, depth, +1)[0]] = 1     #computer turn
        os.system("cls")
        pprint(tic) #print
        if minimax.check(+1)==True:
            print("Computer won, you just can't beat me, senpai!.")
            break
        elif minimax.check(-1)==True:
            print("you have just won!, can't be true.")
            break
        elif depth == 0:
            print("draw!, you can't win!.")
            break
    if input("do you want to try again (y/n)? : ") == "y":
        os.system("cls")
        pprint(tic)
        tic =[0 for i in range(9)]
        continue
    else:break
