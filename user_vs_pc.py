import random
board=[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
def printboard():
    for i in board:
        for r in i:
             print(r+"  ",end="|  ")    
        print()    
        print("----------------") 


def wincheck():
    for i in range(3):
         if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
              return True

    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
         return True
    return False

          
print("Welcome to Tic Tac Toe Game")
print("You are player X and computer is player O")
printboard()
print("start with player X")

player="X"

count=0
while True:
           
        position=int(input("Enter where you want to place your mark (1-9) : "))
        row=(position-1)//3
        col=(position-1)%3

        if board[row][col]=="X" or board[row][col]=="O" :
            print("This position is already filled. Please choose another position.")
            continue

        else:
            board[row][col]=player
            count+=1
            if wincheck():
                 printboard()
                 print("You Win")
                 break
            elif count==9:
                 printboard()
                 print("Draw")
                 break
            pc=random.randint(1,9)
            row=(pc-1)//3
            col=(pc-1)%3
            while  board[row][col] == "X" or board[row][col] == "O":
                   pc=random.randint(1,9)
                   row=(pc-1)//3
                   col=(pc-1)%3
            board[row][col] = "O"
            count+=1
            printboard()
            if wincheck():
                 print("Computer Wins")
                 break
                     
            
          
           

