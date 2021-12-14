class Coordinates:
    '''Documents a unit's coordinates on the battle grid'''
    def __init__(self, x_coor, y_coor,cost = 1):
        self.x = x_coor
        self.y = y_coor
        self.cost = cost

    def location(self):
        ''' Return a tuple of the x,y coordinates of a point '''
        return (self.x, self.y)

    def move_to(self, x_coor, y_coor):
        ''' Assign new coordinates to a point '''
        self.x = x_coor
        self.y = y_coor

    def move(self,x_d,y_d):
        '''Moves a point relative to its original position by the specified distance.'''
        self.x += x_d
        self.y += y_d

        
