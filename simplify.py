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
printboard()
print("start with player X")

player="X"
count=0

while True:    
        position=int(input("Enter where you want to place your mark (1-9) : "))
        if position < 1 or position > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        row=(position-1)//3
        col=(position-1)%3

        if board[row][col]=="X" or board[row][col]=="O" :
            print("This position is already filled. Please choose another position.")
            continue

        else:
            board[row][col]=player
            count+=1
            printboard()
            
            if wincheck():
                 print(f"Player {player} wins!")
                 if input("Do you want to play again? (y/n): ").lower() == 'y':
                     board=[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
                     printboard()
                     player="X"
                     count=0
                     continue
                 break

            elif count==9:
                 print("Draw")
                 if input("Do you want to play again? (y/n): ").lower() == 'y':
                     board=[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
                     printboard()
                     player="X"
                     count=0
                     continue
                 break               
                      
            elif player=="X":
                player="O"
                print("Now player O's turn")
                
            else:
                player="X" 
                print("Now player X's turn")
                

