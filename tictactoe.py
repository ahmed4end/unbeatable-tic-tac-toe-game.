tic =[0,0,0,
      0,0,0,
      0,0,0]

################## AI(computer) best move handling ##################

def minimax(state, depth, alpha=-float('inf'), beta=float('inf'), player=+1):
	best = [-1, -float("inf")] if player == +1 else [-1, +float("inf")]  #best move and score container.
	wins = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))  #wining cominations.
	win = lambda player: any(map(lambda w: state[w[0]]==state[w[1]]==state[w[2]]==player, wins))  #simple winning checker function.
	minimax.check = win #end slot.
	if depth ==0 or win(+1) or win(-1):return [-1, 1 if win(+1) else -1 if win(-1) else 0]  #last branches determiner.
	for cell in [i for i,j in enumerate(state) if j==0]:  #tree view loop.
		state[cell] = player  #move ahead.
		score = minimax(state, depth-1, alpha, beta, -player) #recrusion & backtracking core.
		state[cell] = 0   #move backward
		score[0] = cell   #adding cell position to the score container.
		if player==+1: #maximizing for player +1 (computer).
			best = score if score[1] > best[1] else best #taking maximum value.
			alpha = max(alpha, best[1])  #alpha-beta turn, taking maximum value.
			if alpha >= beta:break #stop exploring branches if alpha finally >= beta.
		else:
			best = score if score[1] < best[1] else best #taking minimum value.
			beta = min(beta, best[1])  #alpha-beta turn, taking minimum value.
			if alpha >= beta:break  #stop exploring branches if alpha finally >= beta.
	return best

################## user interface handling (demo) ##################

def pprint(tic): #printing function for simple view.
    result = []
    for i in range(0,9,3):
        piece  = str(tic[i:i+3]).replace(" 0", " ").replace("0", " ").replace(" -1","x").replace("-1","x").replace(" 1", "o").replace("1", "o").replace(",", " ")
        result.append(piece)
    print("\n".join(result))

pprint(tic)
import os #to clear screen after each move.
while True:
    track= []
    while True:
        while True:
            human = int(input("your turn (1-9): "))-1
            if human in track or human not in range(1,10): #input handling.
                input("you entered invalid position, choose another!")
                os.system("cls")
                pprint(tic)
            else:break
        track.append(human)
        tic[human] = -1
        os.system("cls")
        pprint(tic)
        depth = len([i for i in tic if i == 0])
        ai_move = minimax(tic, depth)[0]
        track.append(ai_move)
        tic[ai_move] = 1     #computer turn
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
    if not input("press any key to try again!, or (n) to quit.") == "n":
        os.system("cls")
        tic =[0 for i in range(9)]
        pprint(tic)
        continue
    else:break
