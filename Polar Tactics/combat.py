def combatForecast(u1,u2):
    #ADD CHECK LATER FOR TERRAIN BONUSES
    dmg1 = u1.u.sl.atk - u2.u.sl.df
    dmg2 = u2.u.sl.atk - u1.u.sl.df
    return (dmg1,dmg2)

def combat(u1,u2,dmgs)
    global u1
    global u2
    u1.u.sl.hp -+ dmgs(1)
    if u1.u.sl.hp < 0:
        u1.u.sl.hp = 0
        
    u2.u.sl.hp -+ dmgs(0)
    if u2.u.sl.hp < 0:
        u2.u.sl.hp = 0
