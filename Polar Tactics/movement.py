import unit
import coordinates


def movepossible(mov,cost):
    '''Checks if movement to this square is possible'''
    if (mov - cost >= 0):
        return True
    else:
        return False
    
#def movement(u):
    
def adjacent(start,mov,old=coordinates.Coordinates(-256,-256)):
    global possible
    possible.append(start)
    #print((start.x,start.y))
    point = coordinates.Coordinates(start.x,start.y) #Check up
    point = coordinates.Coordinates(point.x,point.y+1)
    if not coordSame(point,old):
        if movepossible(mov,point.cost):
            if not coordListCheck(point,possible):
                possible.append(point)
            adjacent(point,mov-point.cost,start)
    point = coordinates.Coordinates(start.x,start.y) #Check right
    point = coordinates.Coordinates(point.x+1,point.y)
    if not coordSame(point,old):
        if movepossible(mov,point.cost):
            if not coordListCheck(point,possible):
                possible.append(point)
            adjacent(point,mov-point.cost,start)
    point = coordinates.Coordinates(start.x,start.y) #Check down
    point = coordinates.Coordinates(point.x,point.y-1)
    if not coordSame(point,old):
        if movepossible(mov,point.cost):
            if not coordListCheck(point,possible):
                possible.append(point)
            adjacent(point,mov-point.cost,start)
    point = coordinates.Coordinates(start.x,start.y) #Check left
    point = coordinates.Coordinates(point.x-1,point.y)
    if not coordSame(point,old):
        if movepossible(mov,point.cost):
            if not coordListCheck(point,possible):
                possible.append(point)
            adjacent(point,mov-point.cost,start)


def possibleMoveCalc(start,mov):
    '''Calculates a list of possible move locations given a point
    and its movement stat.'''
    global possible
    possible = []
    adjacent(start,mov)
    return possible
    
    
    
def coordSame(p1,p2):
    '''Check if two points have the same coordinates.'''
    if ((p1.x == p2.x) and (p1.y == p2.y)):
        return True
    else:
        return False
def coordListCheck(p1,lst):
    for p2 in lst:
        if coordSame(p1,p2):
            return True
    return False

def printPointList(lst):
    for p in lst:
        print((p.x,p.y),end=" ")

def coordPointList(lst):
    lstNew = []
    for p in lst:
        lstNew.append((p.x,p.y))
    lstSort = []
    for item1 in lstNew:
        for item2 in lstNew:
            if item1[0] == item2[0]:
                 if item2 not in lstSort: lstSort.append(item2)
    return lstSort

gervas = unit.Unit("Gervas",[16,8,7,4,5],"bear","gervas.jpg","gervas.png")
a = coordinates.Coordinates(5,2)
test = possibleMoveCalc(a,4)
test2 = coordPointList(test)
print(test2)
