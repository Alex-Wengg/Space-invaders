# I - Import and Initialize
import pygame, random
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480))

class EndPoint(pygame.sprite.Sprite):
    '''Our Bricks class inherits from the Sprite class'''
    def __init__(self,screen):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
           
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((10000, 1))
        self.image.fill((0,200,200)) 
        self.rect = self.image.get_rect()
        self.rect.left =1

        self.rect.top= 345

class Boom(pygame.sprite.Sprite):
    def __init__(self, screen,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.__boom = pygame.image.load("boom.png")
        # Set the image and rect attributes for the bricks
        self.image =self.__boom
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
class Label(pygame.sprite.Sprite):
    '''the method for the labels where we will place the scores the player
    hitting the brick'''
    def __init__(self, message, x_y_center):
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.SysFont("None", 30)
        self.__text = message
        self.__center = x_y_center
    #set the message
    def set_text(self, message):
        self.__text = message
    #constanting displaying the message
    def update(self):

        self.image = self.__font.render(self.__text, 1, (0, 225, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__center


class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__ufo = pygame.image.load("ufo.png")

        # Set the image and rect attributes for the bricks
        self.image =self.__ufo
        
        self.rect = self.image.get_rect()
        self.rect.centerx= 10
        self.rect.centery = 10

    def start(self):
        self.rect.centerx = 10
        self.rect.centery = 10
    def update(self):
        self.rect.centerx += 2
    

class Block(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        self.__right = pygame.image.load("1.png")
        self.__left = pygame.image.load("2.png")
        self.__up = pygame.image.load("3.png")
        self.__down = pygame.image.load("4.png")

        self.__health = [self.__right,self.__right,self.__up,self.__down, 0]

        self.image = self.__health[0]
        self.rect = self.image.get_rect()

        self.rect.left =x+10
        self.rect.y =y
        self.__count = 0



    def hit(self):
        self.__count += 1
        self.image = self.__health[self.__count]
        print (self.__count)
        if self.__count >=4:
            return True

class Line(pygame.sprite.Sprite):
    '''Our Bricks class inherits from the Sprite class'''
    def __init__(self, screen, x, y):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
           
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((1, 10000))
        
        self.image.fill((0,225,0)) 
        self.rect = self.image.get_rect()
        self.rect.left =x

        self.rect.top= y


class Brick(pygame.sprite.Sprite):
    '''Our Bricks class inherits from the Sprite class'''
    def __init__(self, screen,x,y,colour):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
           
        # Set the image and rect attributes for the bricks
        
        self.__speedRate = 250
        self.__dx = 1
        self.__dy = 3
        self.__timer  = 0
        self.__colour = colour
        self.__1small = pygame.image.load("1small.png")
        self.__small2 = pygame.image.load('small2.png')
        self.__medium1 = pygame.image.load('medium1.png')
        self.__medium2 = pygame.image.load('medium2.png')
        self.__fat1 = pygame.image.load('fat1.png')
        self.__fat2 = pygame.image.load('fat2.png')
        self.__boom = pygame.image.load('boom.png')
        self.__alien =[]
        self.__sec = 0
        if self.__colour == 0:
            self.__count = 5
            self.__alien = [self.__1small, self.__small2]
        if self.__colour == 1:
            self.__alien = [self.__medium1, self.__medium2]
            self.__count = 10
        if self.__colour == 2:
            self.__alien = [self.__medium1, self.__medium2]
            self.__count = 15
        if self.__colour == 3:
            self.__alien = [self.__fat1, self.__fat2]
        if self.__colour == 4:
            self.__count = 20
            self.__alien = [self.__fat1, self.__fat2]
        self.image = self.__alien[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        Gone = False
    def die(self, Gone):
        if Gone:
            self.image = self.__boom
            return True

    def change(self):
        self.__dx = -self.__dx
        self.rect.centery += 5
    def faster(self):
        self.__dx += 5
        
    def point(self):
        if self.__colour == 0:
            self.__count = 5
            self.__alien = [self.__1small, self.__small2]
        if self.__colour == 1:
            self.__count = 10
            self.__alien = [self.__medium1, self.__medium2]
        if self.__colour == 2:
            self.__count = 15
            self.__alien = [self.__medium1, self.__medium2]
        if self.__colour == 3:
            self.__count = 20
            self.__alien = [self.__fat1, self.__fat2]
        if self.__colour == 4:
            self.__count = 25
            self.__alien = [self.__fat1, self.__fat2]
        return self.__count


    def update(self):

        self.__sec +=1
        if self.__sec %100 == 0:
            self.image = self.__alien[0]
        elif self.__sec % 50== 0:
            self.image = self.__alien[1]
        self.rect.x += self.__dx
        

class Laser(pygame.sprite.Sprite):
    
    '''This class defines the sprite for our Ball.'''
    def __init__(self,screen, dx , dy):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attr ibutes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((3, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (dx, dy)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y v da ector for the ball.
        self.__screen = screen
        self.__x = 5
        self.__y = 10

    def update(self):
        '''This method causes the x direction of the ball to reverse.'''
        self.rect.top += self.__y

            
class Ball(pygame.sprite.Sprite):
    
    '''This class defines the sprite for our Ball.'''
    def __init__(self,screen, dx , dy):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attr ibutes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((3, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (dx, dy)
        self.__Gone = False
        # Instance variables to keep track of the screen surface
        # and set the initial x and y v da ector for the ball.
        self.__screen = screen
        self.__x = 5
        self.__y = -30
    def die(self, Gone):
        if Gone:
            return True

    def point(self):
        return 4

    def update(self):
        '''This method causes the x direction of the ball to reverse.'''
        self.rect.top += self.__y

class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player 1 and Player 2'''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and player number as
        parameters.  Depending on the player number it loads the appropriate
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes for a black rectangle.
        self.__tank = pygame.image.load('tank.png')

        self.image = self.__tank
        self.rect = self.image.get_rect()
 
        # If we are initializing a sprite for player 1, 
        # position it 10 pixels from screen left.
 
        self.rect.centerx = 10
        # Otherwise, position it 10 pixels from the right of the screen.
        
        # Center the player vertically in the window.
        self.rect.top = 400
        self.__screden = screen
        self.__x = 0
        self.__health = 0
        
    def go_right(self,screen):
        self.__r = True     
        self.__x = 10
    def go_left(self,screen):
        self.__l = True        
        self.__x = -10

    def change(self):
        self.__health += 1

        if self.__health >=300:
            return True
    def update(self):
        self.rect.left += self.__x
        if self.rect.centerx >= 635 and self.__x > 0:
            self.__x = 0
        if self.rect.centerx <= 0 and self.__x <0:
            self.__x = 0
        
def main():
    '''This function defines the 'mainline logic' for our game.'''
      
    # Display
    pygame.display.set_caption("Using Groups To Check Collisions")
     
    # Entities
    screen = pygame.display.set_mode((640, 480))
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    
    pygame.mixer.music.load("sweets.mp3")
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)

    
    screen.blit(background, (0, 0))
    attacklines = []
    walls = []
    player= Player(screen)

    blocks = []

    for defense in range(0,300):
        if defense == 0:
            fill = (255,0,0)
        elif defense == 1:
            fill = (0,0,255)
        elif defense == 2:
            fill = (0,255,0)
        elif defense == 3:
            fill = (0,255,255)        
        block = Block(screen, defense*50, 350)
        blocks.append(block)
    
    for i in range(11):
        for col in range(5):
            if col == 0:
                colour = 0
            elif col == 1:
                colour =1
            elif col == 2:
                colour =2
            elif col == 3:
                colour =3
            elif col == 4:
                colour = 4
            wall = Brick(screen, i*40+40, col*40+40,colour)
            walls.append(wall)
    lines = []
    for j in range(2):
        if j == 0:
            line = Line(screen, 1, 0)
        if j == 1:
            line = Line(screen, 639,0)
        lines.append(line)

    balls =  []
    clock = pygame.time.Clock()
    keepGoing = True
    
    killed=  []
    bonus = Bonus()
    wallGroup = pygame.sprite.Group(walls)
    playerstick = pygame.sprite.Group(player)
    lineGroup = pygame.sprite.Group(lines)
    ball = Ball(screen,1000,1000)

    label = Label("Hi There!", (50,10))
    endpoint = EndPoint(screen)

    allSprites = pygame.sprite.Group( endpoint,walls, player, lines,blocks, bonus, label)
    BigBalls = pygame.sprite.Group( ball)
    Layer =pygame.sprite.Group( player)
    reloading = 5
    time = 0
    Lasers = []
    laser = Laser(screen, player.rect.left, wall.rect.top)
    updatelaser = pygame.sprite.Group(laser)
    updateblock = pygame.sprite.Group(blocks)
    lives =3
    count = 0
    laserreload = 1
    lasertime = 0
    bombGoesOff = 0
    boom = Boom(screen, 2000, 1000)
    killed = 0
    # Loop
    
    while keepGoing:
        # Time
        clock.tick(30)
        time += reloading
        lasertime += laserreload
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left(screen)
                if event.key == pygame.K_d:
                    player.go_right(screen)
                if event.key == pygame.K_SPACE:
                    if time >= 100:
                        time = 0    
                        ball = Ball(screen, player.rect.centerx, player.rect.centery)
                        balls.append(ball)
                        BigBalls = pygame.sprite.Group(ball)

        if pygame.sprite.spritecollide(endpoint, wallGroup,False):
            keepGoing = False
        if pygame.sprite.groupcollide(lineGroup, wallGroup,False, False):
            for wall in walls:
                wall.change()


        for wall in pygame.sprite.groupcollide( wallGroup,BigBalls,True, True):
            boom = Boom(screen, wall.rect.centerx, wall.rect.centery)
            count+= wall.point()
            allSprites.add(boom)
            Gone = True
            killed+=1
            if killed %11 ==0:
                for wall in walls:
                    wall.faster()
            if killed == 23:
                bonus.start()
        bombGoesOff += 1

        if bombGoesOff %10 == 0:
            boom.kill()
        hit=  pygame.sprite.groupcollide(updateblock, updatelaser,False, True)
        for block in hit:
            block.hit()
            if block.hit():
                block.kill()
        if pygame.sprite.spritecollide(player, updatelaser, True):
           player.change()
           lives -=1
           if player.change():
               keepGoing = False
        if pygame.sprite.spritecollide(bonus,BigBalls,  True):
            count += 100
        if lives < 0:
            keepGoing == False
                
        if lasertime >= 60:
            shot = random.choice(walls)
            lasertime = 0
            laser = Laser(screen, shot.rect.centerx, shot.rect.centery)
            Lasers.append(laser)
            updatelaser = pygame.sprite.Group(laser)
        
        label.set_text('             score %d   lives %d' %(count, lives))

        # Refresh screen
        updateblock.clear(screen, background)
        updateblock.update()
        updateblock.draw(screen)
        
        updatelaser.clear(screen, background)
        updatelaser.update()
        updatelaser.draw(screen)
        
        BigBalls.clear(screen, background)
        BigBalls.update()
        BigBalls.draw(screen)
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
      
        pygame.display.flip()
     
    # Close the game window
    pygame.quit()      
# Call the main function
main()
