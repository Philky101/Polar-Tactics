def movepossible(mov,unit,terr):
    '''Checks if movement to this square is possible'''
    if ((mov - terr.cost > 0)) and (unit.clas in terr.classes):
        return True
    else:
        return False

                                                        
