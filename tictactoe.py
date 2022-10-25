from operator import mod
import random

def main():

    px = (input)("Player X, choose your name.")
    po = (input)("Player O, choose your name.")
    print(""" 
    """)

    pxe = bool(px)  
    poe = bool(po)  

    if not pxe: 
        px = "Player X" 
        
    if not poe: 
        po = "Player O" 

    cp = px 

    first = [po + " goes first", px + " goes first"]
    random_str = random.choice(first)

    if random_str == first[0]:
        print(first[0])
        cp = po
        x = 4

    if random_str == first[1]:
        print(first[1])
        cp = px
        x = 1
        
    while px == po:
        print("Both players need to have seperate names.")
        px = (input)("Player X, choose your name.")
        po = (input)("Player O, choose your name.")
             
    b = [" ", " ", " ", " ", " ", " ", " ", " ", " "] 


    def board(cp):
        print (f"""
        
       
    {"It is " + cp + "'s turn." }              
    ┌───────────┬───────────┬───────────┐
    │1          │2          │3          │
    │     {b[0]}     │     {b[1]}     │     {b[2]}     │
    │           │           │           │
    ├───────────┼───────────┼───────────┤
    │4          │5          │6          │
    │     {b[3]}     │     {b[4]}     │     {b[5]}     │
    │           │           │           │
    ├───────────┼───────────┼───────────┤
    │7          │8          │9          │
    │     {b[6]}     │     {b[7]}     │     {b[8]}     │
    │           │           │           │
    └───────────┴───────────┴───────────┘
    """)

        
    board(cp)
        
    def winningO(q, w, e):
        if b[q] == "O" and b[w] == "O" and b[e] == "O":  
            print(po + " wins")
            again = input("Would you like to play again? (Type yes or no) ").lower()
            if again == "yes":
                main()
            if again == "no":
                print("Bye " + px + ", " + po + ".")
                exit()

            else:
                while again != "yes" or "no":
                    yesno2 = input("Choose either yes or no ").lower()
                    if yesno2 == "yes":
                            main()
                    if yesno2 == "no":
                            print("Bye " + px + ", " + po + ".")
                
                            exit()

    def winningX(q, w, e):
        if b[q] == "X" and b[w] == "X" and b[e] == "X":  
                print(po + " wins")
                again = input("Would you like to play again? (Type yes or no) ").lower()
                if again == "yes":
                    main()
                if again == "no":
                    print("Bye " + px + ", " + po + ".")
                    exit()
                else:
                    while again != "yes" or "no":
                        yesno2 = input("Choose either yes or no ").lower()
                        if yesno2 == "yes":
                            main()
                        if yesno2 == "no":
                            print("Bye " + px + ", " + po + ".")
                            exit()

    while x > -1:
        a = input("Choose a slot: ")
        try:
            if b[int(a)-1] == " ":
                if x % 2 == 0:
                    b[int(a)-1] = "O" 
                    board(px)
                else:
                    if x % 2 != 0:
                        cp = px
                        b[int(a)-1] = "X" 
                        board(po)
                x = x + 1
                
            else:
                print("Someone has already played this slot.")
            
        except:
            print("Choose a number between 1-9.")
                
        winningX(0, 1, 2)    

        winningO(0, 1, 2)

        winningX(3, 4, 5)

        winningO(3, 4, 5)

        winningX(6, 7, 8)

        winningO(6, 7, 8)

        winningX(0, 3, 6)

        winningO(0, 3, 6)

        winningX(0, 4, 7)

        winningO(0, 4, 7)

        winningX(2, 5, 8)

        winningO(2, 5, 8)

        winningX(2, 5, 8)

        winningO(0, 4, 8)

        winningX(0, 4, 8)

        winningO(2, 4, 6)

        winningX(2, 4, 6)
        
            
        if (b[0] == "X"  or b[0] == "O" ) and (b[1] == "X"  or b[1] == "O" ) and (b[2] == "X"  or b[2] == "O" ) and (b[3] == "X"  or b[3] == "O" ) and (b[4] == "X"  or b[4] == "O" ) and (b[5] == "X"  or b[5] == "O" ) and (b[6] == "X"  or b[6] == "O" ) and (b[7] == "X"  or b[7] == "O" ) and (b[8] == "X"  or b[8] == "O" ):
            print("The game is a draw.")
            again = input("Would you like to play again? (Type yes or no) ").lower()
            if again == "yes":
                main()
            if again == "no":
                print("Bye " + px + ", " + po + ".")
                exit()
                    
            while again != "yes" or "no":
                yesno2 = input("Choose either yes or no ").lower()
                if yesno2 == "yes":
                    main()
                if yesno2 == "no":
                    print("Bye " + px + ", " + po + ".")
                    exit()                           
main()