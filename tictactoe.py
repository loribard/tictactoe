def gameboard(list_x_o = None,win = None):
    """ This function prints out the gameboard."""


    if list_x_o == None:
        list_x_o = [[" "," "," "],[" "," "," "],[" "," "," "]]
    print list_x_o
    print
    print
    print "Column    0          1          2          "
    print "               |          |               "
    print "Row 0    %s     |     %s    |     %s          " % (list_x_o[0][0],list_x_o[0][1],list_x_o[0][2])
    print "               |          |               " 
    print "       _____________________________"
    print "               |          |              "
    print "Row 1    %s     |     %s    |     %s          " % (list_x_o[1][0],list_x_o[1][1],list_x_o[1][2])
    print "               |          |               " 
    print "       _____________________________"
    print "               |          |               "   
    print "Row 2    %s     |     %s    |     %s         " % (list_x_o[2][0],list_x_o[2][1],list_x_o[2][2])  
    print "               |          |               "      

    if win == True:
        start()
    elif win == False:
        start()
    else:
        new_value(list_x_o)

def new_value(list_x_o):
    """ This function asks the player which number they are and where they want to put their mark."""


    player_num = raw_input("Are you Player 1 or Player 2? (1/2) ")
    player_num = int(player_num)
    new_piece = raw_input("Where would you like to place your mark? (Row,Column) ")
    new_piece = new_piece.split(",")
    row = int(new_piece[0])
    column = int(new_piece[1])
    print new_piece
    place = list_x_o[row][column]


    if place == " ":
        mark(list_x_o,row,column,player_num)
    else:
        print "That space is already taken. Please pick another space for your mark. "
        new_value(list_x_o)


def mark(list_x_o,row,column,player_num):
    """This function puts the mark on the tic tac toe board"""


    if player_num == 1:
        list_x_o[row][column] = "X"
    elif player_num == 2:
        list_x_o[row][column] = "O"

    winner_check(list_x_o,player_num)



    
def winner_check(list_x_o,player_num):
    """ This function checks to see if there is a winner or the  board is full"""



    print "checking for winner"
    if player_num == 1:
        mark = "X"
    else:
        mark = "O"
    condition = False

    if list_x_o[0][0] == mark and list_x_o[0][1] == mark and list_x_o[0][2] == mark:
        condition = True
    elif list_x_o[1][0] == mark and list_x_o[1][1] == mark and list_x_o[1][2] == mark:
        condition = True
    elif list_x_o[2][0] == mark and list_x_o[2][1] == mark and list_x_o[2][2] == mark:
        condition = True
    elif list_x_o[0][0] == mark and list_x_o[1][0] == mark and list_x_o[2][0] == mark:
        condition = True
    elif list_x_o[0][1] == mark and list_x_o[1][1] == mark and list_x_o[2][1] == mark:
        condition = True
    elif list_x_o[0][2] == mark and list_x_o[1][2] == mark and list_x_o[2][2] == mark:
        condition = True
    elif list_x_o[0][0] == mark and list_x_o[1][1] == mark and list_x_o[2][2] == mark:
        condition = True
    elif list_x_o[0][2] == mark and list_x_o[1][1] == mark and list_x_o[2][0] == mark:
        condition = True
    print condition
    if condition == True:
        print "YOU WON!!!!!"
        gameboard(list_x_o,True)
    elif " " not in list_x_o[0] and " " not in list_x_o[1] and " " not in list_x_o[2]:
        print "No winners here"
        gameboard(list_x_o,False)
    else:
        gameboard(list_x_o)

def start():
    play = True
    while play:
        game_play = raw_input("Would you like to play tic tac toe (y/n)? ")
        if game_play == "y":
            play = True
            gameboard()
        else:
            play = False


if __name__ == "__main__":
    start()


           

         