

class Bird:
    def __init__(self,startX,startY,birdPosition):
        self.posX = startX
        self.posY = startY
        self.birdPosition = birdPosition
    
    def moveRight(self):
        self.posY += 1
    
    def moveLeft(self):
        self.posY -= 1

    def moveUp(self):
        self.posX -= 1
    
    def moveDown(self):
        self.posX += 1


class Pig:
    def __init__(self,startX,startY,pigPosition):
        self.posX = startX
        self.posY = startY
        self.pigPosition = pigPosition



class Board:
    def __init__(self,b,p):
        self.b = b
        self.p = p        

    def makeBoard(self):
        self.board = [['*' for i in range(11)]for j in range(11)]

        self.board[self.b.posX][self.b.posY]= self.b.birdPosition
        self.board[self.p.posX][self.p.posY]= self.p.pigPosition

    def displayBoard(self):
        for i in self.board:
            print(' '.join(i))

class Game:
    def main(self):

        b = Bird(1,1,'B')
        p = Pig(1,4,'P')
        status = True
        bd = Board(b,p)
        bd.makeBoard()
        bd.displayBoard()
        while status == True:
            print('What move do you wish to make (r = right)(l = left)(u = up)(d = down)(q = quit game): ')
            inpu = input()
            if inpu == 'r':
                #move right
                bd.b.moveRight()
            elif inpu == 'l':
                #move left
                bd.b.moveLeft()
            elif inpu == 'u':
                #move up
                bd.b.moveUp()
            elif inpu == 'd':
                #move down
                bd.b.moveDown()
            elif inpu == 'q':
                status = False
            else:
                print('input not valid')
        
        print(f'Bird Position: {bd.b.posX} {bd.b.posY}')
        print(f'Pig Position: {bd.p.posX} {bd.p.posY}')
        
        
            

            
            









g = Game()
g.main()