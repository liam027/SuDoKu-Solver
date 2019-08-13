


def check_row(x,y):
    for i in range(1,10):
        for n in range(9):
            if i == my_grid[x][n]:
                if i in my_poss_grid[x][y]:
                    my_poss_grid[x][y].remove(i)


def check_column(x,y):
    for i in range(1,10):
        for n in range(9):
              if i == my_grid[n][y]:
                if i in my_poss_grid[x][y]:
                    my_poss_grid[x][y].remove(i)

def check_box(x,y):
    #box 1
    if x < 3 and y < 3:
        for i in range(1,10):
            for r in range(0,3):
                for c in range(0,3):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 2
    if x > 2 and x < 6 and y < 3:
        for i in range(1,10):
            for r in range(3,6):
                for c in range(0,3):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 3
    if x > 5 and y < 3:
        for i in range(1,10):
            for r in range(6,9):
                for c in range(0,3):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 4
    if x < 3 and y > 2 and y < 6:
        for i in range(1,10):
            for r in range(0,3):
                for c in range(3,6):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 5
    if x > 2 and x < 6 and y > 2 and y < 6:
        for i in range(1,10):
            for r in range(3,6):
                for c in range(3,6):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 6
    if x > 5 and y > 2 and y < 6:
        for i in range(1,10):
            for r in range(6,9):
                for c in range(3,6):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 7
    if x < 3 and y > 5:
        for i in range(1,10):
            for r in range(0,3):
                for c in range(6,9):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 8
    if x > 2 and x < 6 and y > 5:
        for i in range(1,10):
            for r in range(3,6):
                for c in range(6,9):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)
    # box 8
    if x > 5 and y > 5:
        for i in range(1,10):
            for r in range(6,9):
                for c in range(6,9):
                    if i == my_grid[r][c]:
                        if i in my_poss_grid[x][y]:
                            my_poss_grid[x][y].remove(i)

def update_all():
    for i in range(9):
        for n in range(9):
            if my_grid[i][n] == "":
                check_row(i,n)
                check_column(i,n)
                check_box(i,n)
                if len(my_poss_grid[i][n]) == 1:
                    my_grid[i][n] = my_poss_grid[i][n][0]
            else:
                my_poss_grid[i][n] = ""

def is_complete_checker():
    for i in range(9):
        for n in range(9):
            if my_poss_grid[i][n] != "":
                return False
    return True

def Run(x):
    for i in range(x):
        update_all()
        if is_complete_checker() == True:
            print("Puzzle Completed!")
            return

#my_grid = make_grid(9)
#my_poss_grid = make_poss_grid(9)

#print_grid(my_grid)

#Run(10)

#print_grid(my_grid)
#print("/n")
#print_grid(my_poss_grid)
