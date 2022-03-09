import sys

f=open(sys.argv[1],"r")
commands=[[line.split()] for line in f.readlines()]
f.close()
board_dict = {"a8":"R1","b8":"N1","c8":"B1","d8":"QU","e8":"KI","f8":"B2","g8":"N2","h8":"R2","a7":"P1","b7":"P2","c7":"P3","d7":"P4","e7":"P5","f7":"P6","g7":"P7","h7":"P8","a6":"  ","b6":"  ","c6":"  ","d6":"  ","e6":"  ","f6":"  ","g6":"  ","h6":"  ","a5":"  ","b5":"  ","c5":"  ","d5":"  ","e5":"  ","f5":"  ","g5":"  ","h5":"  ","a4":"  ","b4":"  ","c4":"  ","d4":"  ","e4":"  ","f4":"  ","g4":"  ","h4":"  ","a3":"  ","b3":"  ","c3":"  ","d3":"  ","e3":"  ","f3":"  ","g3":"  ","h3":"  ","a2":"p1","b2":"p2","c2":"p3","d2":"p4","e2":"p5","f2":"p6","g2":"p7","h2":"p8","a1":"r1","b1":"n1","c1":"b1","d1":"qu","e1":"ki","f1":"b2","g1":"n2","h1":"r2"}
white_pieces=["r","n","b","k","q","p"]
black_pieces=["R","N","B","K","Q","P"]
square_letter=["a","b","c","d","e","f","g","h"]
square_number=["1","2","3","4","5","6","7","8"]
possibleMoves=[]
left_flag,right_flag,front_flag,back_flag,fld_flag,brd_flag,frd_flag,bld_flag,flag_control = 1,1,1,1,1,1,1,1,0
class move_check():
    def front_move_check(self, front_move, exact_square_letter, a, b):
        global front_flag
        if front_move < 9 and front_flag == 1:
            if board_dict[exact_square_letter + str(front_move)][0:1] in a:
                front_flag = 0
            if board_dict[exact_square_letter + str(front_move)][0:1] in b:
                possibleMoves.append(exact_square_letter + str(front_move))
                front_flag = 0
            if board_dict[exact_square_letter + str(front_move)] == "  ":
                possibleMoves.append(exact_square_letter + str(front_move))
        return possibleMoves
    def back_move_check(self, back_move, exact_square_letter, a, b):
        global back_flag
        if back_move > 0 and back_flag == 1:
            if board_dict[exact_square_letter + str(back_move)][0:1] in a:
                back_flag = 0
            if board_dict[exact_square_letter + str(back_move)][0:1] in b:
                possibleMoves.append(exact_square_letter + str(back_move))
                back_flag = 0
            if board_dict[exact_square_letter + str(back_move)] == "  ":
                possibleMoves.append(exact_square_letter + str(back_move))
        return possibleMoves
    def right_move_check(self, right_move, exact_square_number, a, b):
        global right_flag
        if right_move < 8 and right_flag == 1:
            if board_dict[square_letter[right_move] + exact_square_number][0:1] in a:
                right_flag = 0
            if board_dict[square_letter[right_move] + exact_square_number][0:1] in b:
                possibleMoves.append(square_letter[right_move] + exact_square_number)
                right_flag = 0
            if board_dict[square_letter[right_move] + exact_square_number] == "  ":
                possibleMoves.append(square_letter[right_move] + exact_square_number)
        return possibleMoves
    def left_move_check(self, left_move, exact_square_number, a, b):
        global left_flag
        if left_move >= 0 and left_flag == 1:
            if board_dict[square_letter[left_move] + exact_square_number][0:1] in a:
                left_flag = 0
            if board_dict[square_letter[left_move] + exact_square_number][0:1] in b:
                possibleMoves.append(square_letter[left_move] + exact_square_number)
                left_flag = 0
            if board_dict[square_letter[left_move] + exact_square_number] == "  ":
                possibleMoves.append(square_letter[left_move] + exact_square_number)
        return possibleMoves
    def front_right_move_check(self, front_move, right_move, a, b):
        global frd_flag
        if front_move < 9 and right_move < 8 and frd_flag == 1:
            if board_dict[square_letter[right_move] + str(front_move)][0:1] in a:
                frd_flag = 0
            if board_dict[square_letter[right_move] + str(front_move)][0:1] in b:
                possibleMoves.append(square_letter[right_move] + str(front_move))
                frd_flag = 0
            if board_dict[square_letter[right_move] + str(front_move)] == "  ":
                possibleMoves.append(square_letter[right_move] + str(front_move))
        return possibleMoves
    def front_left_move_check(self, front_move, left_move, a, b):
        global fld_flag
        if front_move <9 and left_move >=0 and fld_flag==1:
            if board_dict[square_letter[left_move] + str(front_move)][0:1] in a:
                fld_flag = 0
            if board_dict[square_letter[left_move] + str(front_move)][0:1] in b:
                possibleMoves.append(square_letter[left_move] + str(front_move))
                fld_flag = 0
            if board_dict[square_letter[left_move] + str(front_move)] == "  ":
                possibleMoves.append(square_letter[left_move] + str(front_move))
        return possibleMoves
    def back_right_move_check(self, back_move, right_move, a, b):
        global brd_flag
        if back_move > 0 and right_move < 8 and brd_flag == 1:
            if board_dict[square_letter[right_move] + str(back_move)][0:1] in a:
                brd_flag = 0
            if board_dict[square_letter[right_move] + str(back_move)][0:1] in b:
                possibleMoves.append(square_letter[right_move] + str(back_move))
                brd_flag = 0
            if board_dict[square_letter[right_move] + str(back_move)] == "  ":
                possibleMoves.append(square_letter[right_move] + str(back_move))
        return possibleMoves
    def back_left_move_check(self, back_move, left_move, a, b):
        global bld_flag
        if back_move >0 and left_move>=0 and bld_flag == 1:
            if board_dict[square_letter[left_move] + str(back_move)][0:1] in a:
                bld_flag = 0
            if board_dict[square_letter[left_move] + str(back_move)][0:1] in b:
                possibleMoves.append(square_letter[left_move] + str(back_move))
                bld_flag = 0
            if board_dict[square_letter[left_move] + str(back_move)] == "  ":
                possibleMoves.append(square_letter[left_move] + str(back_move))
        return possibleMoves
def chessboard():
    N=0
    print("------------------------")
    for i in range(8):
        test_list=list(board_dict.values())[N:N+8]
        print(" ".join(["{0}".format(k) for k in test_list]))
        N=N+8
    print("------------------------")
def showmoves(chess_piece):
    global board_dict
    global flag_control
    global flag_control2
    if chess_piece in board_dict.values():
        key_list = list(board_dict.keys())
        val_list = list(board_dict.values())
        exact_square_index=val_list.index(chess_piece)
        global possibleMoves
        possibleMoves=[]
        if chess_piece in board_dict.values():
            exact_square=key_list[exact_square_index]
        global left_flag, right_flag, front_flag, back_flag, brd_flag, bld_flag, frd_flag, fld_flag
        if chess_piece[:1] =="p" or chess_piece[:1] =="P":
            if chess_piece[:1] =="p":
                a=white_pieces
                dif=1
            else:
                a=black_pieces
                dif=-1
            next_square=str(exact_square[0:1])+str(int(exact_square[1:2])+dif)
            possibleMoves.append(str(exact_square[0:1])+str(int(exact_square[1:2])+dif))
            if board_dict[next_square][0:1] in a:
                return "FAILED"
        if chess_piece[:1] =="r" or chess_piece[:1] =="R":
            if chess_piece[:1] =="r":
                a,b=white_pieces,black_pieces
            else:
                a,b=black_pieces,white_pieces
            exact_square_number=exact_square[1:2]
            exact_square_letter=exact_square[0:1]
            d1=square_number.index(exact_square_number)
            d2 = square_letter.index(exact_square_letter)
            for n in range(1,8):
                front_move=int(square_number[d1])+n
                back_move=int(square_number[d1])-n
                left_move = d2-n
                right_move= d2 + n
                possibleMoves=move_check().front_move_check(front_move,exact_square_letter,a,b)
                possibleMoves=move_check().back_move_check(back_move,exact_square_letter,a,b)
                possibleMoves=move_check().right_move_check(right_move, exact_square_number, a, b)
                possibleMoves=move_check().left_move_check(left_move, exact_square_number, a, b)
            left_flag, right_flag, front_flag, back_flag = 1, 1, 1, 1
        if chess_piece[:1] =="b" or chess_piece[:1] =="B":
            if chess_piece[:1] =="b":
                back_control=0
            else:
                back_control=1
            if chess_piece[:1] =="b":
                a=white_pieces
                b =black_pieces
            else:
                a = black_pieces
                b = white_pieces
            exact_square_number = exact_square[1:2]
            exact_square_letter = exact_square[0:1]
            d1 = square_number.index(exact_square_number)
            d2 = square_letter.index(exact_square_letter)
            for n in range(1,8):
                front_move=int(square_number[d1])+n
                back_move=int(square_number[d1])-n
                left_move = d2-n
                right_move= d2 + n
                if back_control==0:
                    possibleMoves = move_check().front_right_move_check(front_move, right_move, a, b)
                    possibleMoves = move_check().front_left_move_check(front_move, left_move, a, b)
                else:
                    possibleMoves = move_check().back_right_move_check(back_move, right_move, a, b)
                    possibleMoves = move_check().back_left_move_check(back_move, left_move, a, b)
            left_flag, right_flag, front_flag, back_flag = 1, 1, 1, 1
            brd_flag, bld_flag, frd_flag, fld_flag = 1, 1, 1, 1
        if chess_piece[:1] =="n" or chess_piece[:1] =="N":
            if chess_piece[:1] =="n":
                a=white_pieces
                b=black_pieces
            else:
                a=black_pieces
                b=white_pieces
            exact_square_number = exact_square[1:2]
            exact_square_letter = exact_square[0:1]
            d1 = square_number.index(exact_square_number)
            d2 = square_letter.index(exact_square_letter)
            fld_flag,brd_flag,frd_flag,bld_flag,brL_flag,blL_flag = 1,1,1,1,1,1
            for n in range(1, 2):
                front_move = int(square_number[d1]) + n
                back_move = int(square_number[d1]) - n
                left_move = d2 - n
                right_move = d2 + n
                if front_move < 9 and right_move < 8 and frd_flag == 1:
                    if board_dict[square_letter[right_move] + str(front_move)][0:1] in a:
                        frd_flag = 0
                    if board_dict[square_letter[right_move] + str(front_move)][0:1] in b:
                        frd_flag = 0
                    if board_dict[square_letter[right_move] + str(front_move)] == "  ":
                        possibleMoves.append(square_letter[right_move] + str(front_move))
                if front_move < 9 and left_move >= 0 and fld_flag == 1:
                    if board_dict[square_letter[left_move] + str(front_move)][0:1] in a:
                        fld_flag = 0
                    if board_dict[square_letter[left_move] + str(front_move)][0:1] in b:
                        fld_flag = 0
                    if board_dict[square_letter[left_move] + str(front_move)] == "  ":
                        possibleMoves.append(square_letter[left_move] + str(front_move))
                if back_move > 0 and right_move < 8 and brd_flag == 1:
                    if board_dict[square_letter[right_move] + str(back_move)][0:1] in a:
                        brd_flag = 0
                    if board_dict[square_letter[right_move] + str(back_move)][0:1] in b:
                        brd_flag = 0
                    if board_dict[square_letter[right_move] + str(back_move)] == "  ":
                        possibleMoves.append(square_letter[right_move] + str(back_move))
                if back_move > 0 and left_move >= 0 and bld_flag == 1:
                    if board_dict[square_letter[left_move] + str(back_move)][0:1] in a:
                        bld_flag = 0
                    if board_dict[square_letter[left_move] + str(back_move)][0:1] in b:
                        bld_flag = 0
                    if board_dict[square_letter[left_move] + str(back_move)] == "  ":
                        possibleMoves.append(square_letter[left_move] + str(back_move))
            left_flag, right_flag, front_flag, back_flag = 1, 1, 1, 1
            brd_flag, bld_flag, frd_flag, fld_flag = 1, 1, 1, 1
            test1=1
            test2=2
            temp=test1
            for n in range(1,3):
                front_move=int(square_number[d1])+test1
                back_move=int(square_number[d1])-test1
                left_move = d2-test2
                right_move =d2+test2
                if front_move <9 and right_move <8 and frd_flag==1:
                    if board_dict[square_letter[right_move]+str(front_move)][0:1] in b :
                        possibleMoves.append(square_letter[right_move]+str(front_move))
                    if board_dict[square_letter[right_move] + str(front_move)]=="  ":
                        possibleMoves.append(square_letter[right_move]+str(front_move))
                if front_move <9 and left_move >=0 and fld_flag==1:
                    if board_dict[square_letter[left_move]+str(front_move)][0:1] in b :
                        possibleMoves.append(square_letter[left_move]+str(front_move))
                    if board_dict[square_letter[left_move]+str(front_move)]=="  ":
                        possibleMoves.append(square_letter[left_move]+str(front_move))
                if back_move > 0 and right_move<8 and brd_flag == 1:
                    if board_dict[square_letter[right_move]+str(back_move)][0:1] in b :
                        possibleMoves.append(square_letter[right_move]+str(back_move))
                    if board_dict[square_letter[right_move]+str(back_move)]=="  ":
                        possibleMoves.append(square_letter[right_move]+str(back_move))
                if back_move >0 and left_move>=0 and bld_flag == 1:
                    if board_dict[square_letter[left_move]+str(back_move)][0:1] in b :
                        possibleMoves.append(square_letter[left_move]+str(back_move))
                    if board_dict[square_letter[left_move]+str(back_move)]=="  ":
                        possibleMoves.append(square_letter[left_move]+str(back_move))
                test1 = test2
                test2 = temp
        if chess_piece[:2] =="qu" or chess_piece[:2] =="QU":
            if chess_piece[:2] =="qu":
                a,b=white_pieces,black_pieces
            else:
                a,b=black_pieces,white_pieces
            exact_square_number,exact_square_letter=exact_square[1:2],exact_square[0:1]
            d1,d2=square_number.index(exact_square_number),square_letter.index(exact_square_letter)
            for n in range(1,8):
                front_move,back_move,left_move,right_move=int(square_number[d1])+n,int(square_number[d1])-n,d2-n,d2 +n
                possibleMoves=move_check().front_move_check(front_move,exact_square_letter,a,b)
                possibleMoves=move_check().back_move_check(back_move,exact_square_letter,a,b)
                possibleMoves=move_check().right_move_check(right_move, exact_square_number, a, b)
                possibleMoves=move_check().left_move_check(left_move, exact_square_number, a, b)
                possibleMoves = move_check().front_right_move_check(front_move, right_move, a, b)
                possibleMoves = move_check().front_left_move_check(front_move, left_move, a, b)
                possibleMoves = move_check().back_right_move_check(back_move, right_move, a, b)
                possibleMoves = move_check().back_left_move_check(back_move, left_move, a, b)
            left_flag,right_flag,front_flag,back_flag,brd_flag,bld_flag,frd_flag,fld_flag = 1,1,1,1,1,1,1,1
        if chess_piece[:2] =="ki" or chess_piece[:2] =="KI":
            if chess_piece[:2] =="ki":
                a,b=white_pieces,black_pieces
            else:
                a,b=black_pieces,white_pieces
            exact_square_number,exact_square_letter=exact_square[1:2],exact_square[0:1]
            d1, d2 =square_number.index(exact_square_number),square_letter.index(exact_square_letter)
            for n in range(1,2):
                front_move=int(square_number[d1])+n
                back_move=int(square_number[d1])-n
                left_move = d2-n
                right_move= d2 + n
                possibleMoves = move_check().front_move_check(front_move, exact_square_letter, a, b)
                possibleMoves = move_check().back_move_check(back_move, exact_square_letter, a, b)
                possibleMoves = move_check().right_move_check(right_move, exact_square_number, a, b)
                possibleMoves = move_check().left_move_check(left_move, exact_square_number, a, b)
                possibleMoves = move_check().front_right_move_check(front_move, right_move, a, b)
                possibleMoves = move_check().front_left_move_check(front_move, left_move, a, b)
                possibleMoves = move_check().back_right_move_check(back_move, right_move, a, b)
                possibleMoves = move_check().back_left_move_check(back_move, left_move, a, b)
            left_flag,right_flag,front_flag,back_flag = 1, 1, 1, 1
            brd_flag, bld_flag, frd_flag, fld_flag = 1, 1, 1, 1
        if flag_control == 0 :
            possibleMoves = sorted(possibleMoves)
            for i in possibleMoves:
                if i!=possibleMoves[-1]:
                    print(i,end=" ")
                else:
                    print(i)
        flag_control= 0
        flag_control2 = 1
        if len(possibleMoves)==0:
            print("FAILED")
            flag_control2 = 0
def move(chess_piece,piece_step):
    global possibleMoves
    global board_dict
    global flag_control
    king=[]
    possibleMoves=[]
    flag_control = 1
    showmoves(chess_piece)
    for key,value in board_dict.items():
        if board_dict[key]=="ki" or board_dict[key]=="KI":
            king.append(key)
    for i in possibleMoves:
        for j in king:
            if i == j :
                possibleMoves.remove(j)
    exact_step=""
    flagX=0
    for key, value in board_dict.items():
        if value == chess_piece:
            exact_step=key
    for step in possibleMoves:
        if step==piece_step:
            board_dict[step]=chess_piece
            board_dict[exact_step]="  "
            print("OK")
            flagX=1
            break
    if flagX==0 and flag_control2==1:
        print("FAILED")
def initialize():
    global board_dict
    board_dict = {"a8": "R1", "b8": "N1", "c8": "B1", "d8": "QU", "e8": "KI", "f8": "B2", "g8": "N2", "h8": "R2",
                  "a7": "P1", "b7": "P2", "c7": "P3", "d7": "P4", "e7": "P5", "f7": "P6", "g7": "P7", "h7": "P8",
                  "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
                  "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
                  "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
                  "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
                  "a2": "p1", "b2": "p2", "c2": "p3", "d2": "p4", "e2": "p5", "f2": "p6", "g1": "p7", "h2": "p8",
                  "a1": "r1", "b1": "n1", "c1": "b1", "d1": "qu", "e1": "ki", "f1": "b2", "g2": "n2", "h1": "r2"}
    chessboard()
n = 0
for i in range(len(commands)):
    if commands[n][0][0] =="move":
        print(">",commands[n][0][0],commands[n][0][1],commands[n][0][2])
        move(commands[n][0][1],commands[n][0][2])
    if commands[n][0][0] == "showmoves":
        print(">",commands[n][0][0],commands[n][0][1])
        showmoves(commands[n][0][1])
    if commands[n][0][0] == "print":
        print(">",commands[n][0][0])
        chessboard()
    if commands[n][0][0] == "initialize":
        print(">",commands[n][0][0])
        print("OK")
        initialize()
    if commands[n][0][0] == "exit":
        print(">",commands[n][0][0])
        exit()
    n += 1
