from XorO import Board,Player,AbBot,Choice
import copy
import math


# Создаем экземпляр класса AbBot



# Создаем экземпляр класса Board
def strt():
    
    
    if input("За кого вы играете") =="o":
        bot = AbBot(Player.o)  # Используйте Player.x, если хотите, чтобы бот был крестиком
        plr=Player.x
    else:
        bot = AbBot(Player.x)  # Используйте Player.x, если хотите, чтобы бот был крестиком
        plr=Player.o
        
    board = Board()

    while True:
        if plr!=Player.o:
            fy=int(input("номер клетки "))
            dy,dx=math.floor(fy/3),fy%3
            print(dx-1,dy)
            if dx-1==-1:
                dx,dy=3,dy-1
                print(dx-1,dy)
            print(dx-1,dy)
            board.make_move(dy,dx-1,plr)
            board.print()
            # Выбираем ход для бота
        
        bot_choice = bot.select_move(board)
        try:
            by=bot_choice[0]
            bx=bot_choice[1]
            board.make_move(by,bx,bot.player)
            # В bot_choice теперь будет содержаться координата, куда бот поставит нолик
            print("Бот поставит нолик в клетку:", bot_choice)
            board.print()
            if plr!=Player.x:
                fy=int(input("номер клетки "))
                dy,dx=math.floor(fy/3),fy%3
                print(dx-1,dy)
                if dx-1==-1:
                    dx,dy=3,dy-1
                    print(dx-1,dy)
                print(dx-1,dy)
                board.make_move(dy,dx-1,plr)
                board.print()
                # Выбираем ход для бота
        except:
            
            input()
            strt()
            break

   
