import random
M = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]
N= [
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ]
cont = 0

#creazione tavola
max = 0
while not(max>9 and max<51):
    max = int(input("how many bombs (10 to 50)? "))
for n in range(0,max):
    i = random.randint(0,9)
    j = random.randint(0,9)
    M[i][j] = "*"

#prima riga
if M[0][0] != '*':
    if M[0][1] == '*':
        cont += 1
    if M[1][0] == '*':
        cont += 1
    if M[1][1] == '*':
        cont += 1
    M[0][0] = cont
    cont = 0
i = 0
for j in range(1,9):
    if M[i][j] != '*':
        if M[i][j+1] == '*':
            cont += 1
        if M[i][j-1] == '*':
            cont += 1
        if M[i+1][j+1] == '*':
            cont += 1
        if M[i+1][j-1] == '*':
            cont += 1
        if M[i+1][j] == '*':
            cont += 1
        M[i][j] = cont
        cont = 0
if M[0][9] != '*':
    if M[0][8] == '*':
        cont += 1
    if M[1][9] == '*':
        cont += 1
    if M[1][8] == '*':
        cont += 1
    M[0][9] = cont
    cont = 0
    
        
  
#centro
for i in range(1,9):
    if M[i][0] != '*':
        if M[i][1] == '*':
            cont += 1
        if M[i+1][0] == '*':
            cont += 1
        if M[i+1][1] == '*':
            cont += 1
        if M[i-1][0] == '*':
            cont += 1
        if M[i-1][1] == '*':
            cont += 1
        M[i][0] = cont
        cont = 0
    for j in range(1,9):
        if M[i][j] != '*':
            if M[i][j+1] == '*':
                cont += 1
            if M[i][j-1] == '*':
                cont += 1
            if M[i+1][j+1] == '*':
                cont += 1
            if M[i+1][j-1] == '*':
                cont += 1
            if M[i+1][j] == '*':
                cont += 1
            if M[i-1][j+1] == '*':
                cont += 1
            if M[i-1][j-1] == '*':
                cont += 1
            if M[i-1][j] == '*':
                cont += 1
            M[i][j] = cont
            cont = 0
    if M[i][9] != '*':
        if M[i][8] == '*':
            cont += 1
        if M[i+1][9] == '*':
            cont += 1
        if M[i+1][8] == '*':
            cont += 1
        if M[i-1][9] == '*':
            cont += 1
        if M[i-1][8] == '*':
            cont += 1
        M[i][9] = cont
        cont = 0
        
#ultima riga
if M[9][0] != '*':
    if M[9][1] == '*':
        cont += 1
    if M[8][0] == '*':
        cont += 1
    if M[8][1] == '*':
        cont += 1
    M[9][0] = cont
    cont = 0
i = 9
for j in range(1,9):
    if M[i][j] != '*':
        if M[i][j+1] == '*':
            cont += 1
        if M[i][j-1] == '*':
            cont += 1
        if M[i-1][j+1] == '*':
            cont += 1
        if M[i-1][j-1] == '*':
            cont += 1
        if M[i-1][j] == '*':
            cont += 1
        M[i][j] = cont
        cont = 0
if M[9][9] != '*':
    if M[9][8] == '*':
        cont += 1
    if M[8][9] == '*':
        cont += 1
    if M[8][8] == '*':
        cont += 1
    M[9][9] = cont
    cont = 0


#funzione zeri
def zero(ci,cj):
    if ci == 0:
        if cj == 0:
            N[ci][cj+1] = M[ci][cj+1]
            N[ci+1][cj] = M[ci+1][cj]
            N[ci+1][cj+1] = M[ci+1][cj+1]
        elif cj == 9:
            N[ci][cj-1] = M[ci][cj-1]
            N[ci+1][cj] = M[ci+1][cj]
            N[ci+1][cj-1] = M[ci+1][cj-1]
        else:
            N[ci][cj+1] = M[ci][cj+1]
            N[ci+1][cj] = M[ci+1][cj]
            N[ci+1][cj+1] = M[ci+1][cj+1]
            N[ci+1][cj-1] = M[ci+1][cj-1]
            N[ci][cj-1] = M[ci][cj-1]
    elif ci == 9:
        if cj == 0:
            N[ci][cj+1] = M[ci][cj+1]
            N[ci-1][cj] = M[ci-1][cj]
            N[ci-1][cj+1] = M[ci-1][cj+1]
        elif cj == 9:
            N[ci][cj-1] = M[ci][cj-1]
            N[ci-1][cj] = M[ci-1][cj]
            N[ci-1][cj-1] = M[ci-1][cj-1]
        else:
            N[ci][cj+1] = M[ci][cj+1]
            N[ci-1][cj] = M[ci-1][cj]
            N[ci-1][cj+1] = M[ci-1][cj+1]
            N[ci][cj-1] = M[ci][cj-1]
            N[ci-1][cj-1] = M[ci-1][cj-1]
    else:
        if cj == 0:
            N[ci][cj+1] = M[ci][cj+1]
            N[ci+1][cj+1] = M[ci+1][cj+1]
            N[ci-1][cj+1] = M[ci-1][cj+1]
            N[ci+1][cj] = M[ci+1][cj]
            N[ci-1][cj] = M[ci-1][cj]
        elif cj == 9:
            N[ci][cj-1] = M[ci][cj-1]
            N[ci+1][cj-1] = M[ci+1][cj-1]
            N[ci-1][cj-1] = M[ci-1][cj-1]
            N[ci+1][cj] = M[ci+1][cj]
            N[ci-1][cj] = M[ci-1][cj]
        else:
            N[ci+1][cj+1] = M[ci+1][cj+1]
            N[ci+1][cj] = M[ci+1][cj]
            N[ci+1][cj-1] = M[ci+1][cj-1]
            N[ci-1][cj+1] = M[ci-1][cj+1]
            N[ci-1][cj] = M[ci-1][cj]
            N[ci-1][cj-1] = M[ci-1][cj-1]
            N[ci][cj-1] = M[ci][cj-1]
            N[ci][cj+1] = M[ci][cj+1]


   
#main
end = False
while not end:

    flag = True
    for mi in range (0,10):
        for mj in range(0,10):
            if M[mi][mj] == 0 and N[mi][mj] != 0:
                flag = False
            if M[mi][mj] == 1 and N[mi][mj] != 1:
                flag = False
            if M[mi][mj] == 2 and N[mi][mj] != 2:
                flag = False
            if M[mi][mj] == 3 and N[mi][mj] != 3:
                flag = False
            if M[mi][mj] == 4 and N[mi][mj] != 4:
                flag = False
            if M[mi][mj] == 5 and N[mi][mj] != 5:
                flag = False
            if M[mi][mj] == 6 and N[mi][mj] != 6:
                flag = False
            if M[mi][mj] == 7 and N[mi][mj] != 7:
                flag = False
            if M[mi][mj] == 8 and N[mi][mj] != 8:
                flag = False
    if flag == True:
        print("\n\tYOU WIN ")
        end = True
        break
            


    for a in range(0,10):
        for ai in range(0,10):
            for aj in range(0,10):
                if N[ai][aj] == 0:
                    zero(ai,aj)
                
                
    
    #stampa
    for n in range(0,10):
        print(n,"   ",N[n][0],N[n][1],N[n][2],N[n][3],N[n][4],N[n][5],N[n][6],N[n][7],N[n][8],N[n][9])
    print("\n")
    print("     ","A B C D E F G H I L")

    
    #gioco
    c = input("\ncoordinates: ")
    if len(c) != 2:
        continue
    if c[1].isdecimal() == False:
        continue
    else:
        ci = int(c[1])
    if c[0] == "A" or c[0] == "a":
        cj = 0
    elif c[0] == "B" or c[0] == "b":
        cj = 1
    elif c[0] == "C" or c[0] == "c":
        cj = 2
    elif c[0] == "D" or c[0] == "d":
        cj = 3
    elif c[0] == "E" or c[0] == "e":
        cj = 4
    elif c[0] == "F" or c[0] == "f":
        cj = 5
    elif c[0] == "G" or c[0] == "g":
        cj = 6
    elif c[0] == "H" or c[0] == "h":
        cj = 7
    elif c[0] == "I" or c[0] == "i":
        cj = 8
    elif c[0] == "L" or c[0] == "l":
        cj = 9
    else:
        continue
    m = input("flag or dig (f/d)? ")
    if m == "f":
        N[ci][cj] = "P"
        continue
    if m == "d":
        if M[ci][cj] == "*":
            print("\n\tYOU LOSE ")
            end = True
        elif M[ci][cj] == 0:
            N[ci][cj] = M[ci][cj]
            zero(ci,cj)
        else:
            N[ci][cj] = M[ci][cj]
