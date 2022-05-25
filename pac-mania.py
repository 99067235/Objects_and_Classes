class ghosts:
    def __init__(self,color,state,startPos,speed):
        self.state = state
        self.color = color
        self.coords = startPos
        self.speed = speed

class pacPerson:
    def __init__(self, lives = 0, speed = 0, startPosition = ""):
        self.speed = speed
        self.coords = startPosition
        self.lives = lives
    
    def grabFood():
        pass
    
    def respawn():
        pass

pacMan = pacPerson(3,10, "1,1,1")
pinky = ghosts("pink", "follow", "0,0,0", "5")
blinky = ghosts("blue", "wander", "1,0,0", "7")