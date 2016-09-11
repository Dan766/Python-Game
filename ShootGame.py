'''
  _________                         _________                _____  __                              
 /   _____/__________    ____  ____ \_   ___ \____________ _/ ____\/  |_                            
 \_____  \\____ \__  \ _/ ___\/ __ \/    \  \/\_  __ \__  \\   __\\   __\                           
 /        \  |_> > __ \\  \__\  ___/\     \____|  | \// __ \|  |   |  |                             
/_______  /   __(____  /\___  >___  >\______  /|__|  (____  /__|   |__|                             
        \/|__|       \/     \/    \/        \/            \/                                        
                                                                                                    
  ______   ______   ______   ______   ______   ______   ______   ______                             
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/                             
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/                             
                                                                                                    
                                                                                                    
__________             ________                                     .___    _____  .__ __           
\______   \___.__. /\  \______ \ _____    ____   _____    ____    __| _/   /     \ |__|  | __ ____  
 |    |  _<   |  | \/   |    |  \\__  \  /    \  \__  \  /    \  / __ |   /  \ /  \|  |  |/ // __ \ 
 |    |   \\___  | /\   |    `   \/ __ \|   |  \  / __ \|   |  \/ /_/ |  /    Y    \  |    <\  ___/ 
 |______  // ____| \/  /_______  (____  /___|  / (____  /___|  /\____ |  \____|__  /__|__|_ \\___  >
        \/ \/                  \/     \/     \/       \/     \/      \/          \/        \/    \/ 
'''
#Imports the pygame module used in drawing 
import pygame
#imports the random module used for generating random values
import random
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREEN = (20,202,20)

# Initialize Pygame
pygame.init()
# Set the height and width of the screen
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])

# Declares Fonts
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 20)

#Initializes All the Global variables used in the program
new = True
gameover = [False, "Invalid"]
screencount = 0
GlobalSpeed = 60
spawncounter = 0
seconds = 0
High_score = 0
GlobalSpeed_Counter = 0
ShieldBar = 100
GlobalSpeed_Counter2 = 0
GlobalSpeed_Counter3 = 0
Shooting_Counter = 0
Shoot = False
x = 10
y = 100
Level = 1
xspeed = 0
Bullet_Type = "Reg"
score = 0
MainGame = True
backgroundImage = pygame.image.load('lvl1.jpg').convert()
player_Health = 100
player_Counter = 0
player_Shield = 100
lvl=1
gamedone = False
rect = pygame.mouse.get_pos()
done = False
ContactDeath = False
Text_Count = 50
player_count = 0
Text_Amo = "Out of Ammo"
AmoText = font.render("" + str(Text_Amo), True, WHITE)
Lowhealth_Counter = 0
LowhealthText = font.render("" + str("Low Health"), True, WHITE)
SlowmoText = font.render("" + str("Focus Restored: Press SPACE To Activate!"), True, WHITE)

# --- Sprite lists --- #
# Creates all my sprite lists
all_sprites_list = pygame.sprite.Group()
hardbullet_list = pygame.sprite.Group()
block_hit_list = pygame.sprite.Group()
block_bullet_list= pygame.sprite.Group()
Icon_list = pygame.sprite.Group()
playerlist = pygame.sprite.Group()
block_list = pygame.sprite.Group()
disk_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
Animate_list = pygame.sprite.Group()

px = 90
py = 140
#Creates the Player Animated Sprite
PlayerSprite = []
image = pygame.image.load('ani_ship_0.gif').convert_alpha()
PlayerSprite.append(pygame.transform.scale(image, [px,py]) )

image = pygame.image.load('ani_ship_1.gif').convert_alpha()
PlayerSprite.append(pygame.transform.scale(image, [px,py]) )

image = pygame.image.load('ani_ship_2.gif').convert_alpha()
PlayerSprite.append(pygame.transform.scale(image, [px,py]) )

image = pygame.image.load('ani_ship_3.gif').convert_alpha()
PlayerSprite.append(pygame.transform.scale(image, [px,py]) )

#Creates the list containing te enemy explosion animations
px = 50
py = 50
EnemyDeath2 = []
image = pygame.image.load('mp-0.gif').convert_alpha()
image = pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-1.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-2.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-3.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-4.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-5.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-6.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-7.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-8.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)
image = pygame.image.load('mp-9.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath2.append(image)

#creates the enemy 3 death animation
EnemyDeath3 = []
for image in EnemyDeath2:
    image = pygame.transform.scale(image, [150,150])
    EnemyDeath3.append(image)
print(len(EnemyDeath3))

#Creates the list containing te enemy explosion animations
px = 200
py = 300
EnemyDeath5 = []
image = pygame.image.load('t0.gif').convert_alpha()
image = pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t1.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t2.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t3.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t4.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t5.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t6.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t7.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t8.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t9.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t10.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t11.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t12.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t13.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t14.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t15.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)
image = pygame.image.load('t16.gif').convert_alpha()
image =pygame.transform.scale(image, [px,py])
EnemyDeath5.append(image)



#Creates the list containing all the images used in the enemy death animations
EnemyDeath = []
image = pygame.image.load('tmp0.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp1.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp2.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp3.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp4.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp5.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp6.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp7.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp8.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp9.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp10.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp11.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp12.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp13.gif').convert_alpha()
EnemyDeath.append(image)
image = pygame.image.load('tmp14.gif').convert_alpha()
EnemyDeath.append(image)


#Creates the fireball list and appends all images used for the power 3 animation (fireshot)
fireball = []
image = pygame.image.load('tmp-0.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-1.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-2.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-3.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-4.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-5.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-6.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-7.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-8.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-9.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-10.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-11.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-12.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-13.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-14.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-15.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-16.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-17.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-18.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-19.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-20.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-21.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-22.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-23.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-24.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-25.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-26.gif').convert_alpha()
fireball.append(image)
image = pygame.image.load('tmp-27.gif').convert_alpha()
fireball.append(image)

#----------------Default Bullet Ammo---------------------#
#Sets the starting bullet ammo of each power
#Power1 Amo = unlimited
Power2_Amo = 10
Power3_Amo = 2
Power4_Amo = 5
Power5_Amo = 0
 
 

#Initializes all sounds used in game 
RegShot = pygame.mixer.Sound("RegShot.ogg")
DoubleShot = pygame.mixer.Sound("DoubleShot.ogg")
FireShot = pygame.mixer.Sound("FireShot.ogg")
PierceShot = pygame.mixer.Sound("PierceShot.ogg")
Powerup = pygame.mixer.Sound("Powerup.ogg")
Slowmo = pygame.mixer.Sound("SlowMotion.ogg")

#Sets the sound volume to .3
Powerup.set_volume(0.3)

#Sets the screen caption to "SpaceCraft"
pygame.display.set_caption("SpaceCraft")


# Loads Background Images
winner = pygame.image.load('winner.png').convert_alpha()
loseScreen = pygame.image.load('loseScreen.png').convert_alpha()

# Function used for loading backgrond images
def LoadBack(file):
    screen.blit(file, [0,0])

time = 0
timer = 0

#-----------------------------SPRITE/OBJECT CREATION FUNCTIONS--------------------------#
#Function used to create the clickable powerup icons on the screen
def CreatePower(amount,typ, screen_width, screen_height, startx, starty):
    for i in range(amount):
        if typ == 2:
            #Set bullet equal to the power class
            bullet = Power2()
            bullet.typ = 2
            #Randomly Place the power on the screen
            bullet.rect.x = random.randrange(startx, screen_width)
            bullet.rect.y = random.randrange(starty, screen_height)
            # Add the icon to the lists
            all_sprites_list.add(bullet)
            Icon_list.add(bullet)
            bullet = Power2()
        if typ == 3:
            #Set bullet equal to the power class
            bullet = Power3()
            bullet.typ = 3
            #Randomly Place the power on the screen
            bullet.rect.x = random.randrange(startx, screen_width)
            bullet.rect.y = random.randrange(starty, screen_height)
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            Icon_list.add(bullet)
            bullet = Power3()
        if typ == 4:
            #Set bullet equal to the power class
            bullet = Power4()
            bullet.typ = 4
            #Randomly Place the power on the screen
            bullet.rect.x = random.randrange(startx, screen_width)
            bullet.rect.y = random.randrange(starty, screen_height)
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            Icon_list.add(bullet)
            bullet = Power4()
    
##Function used to create the bullets shot by the Enemy 
def Enemy_Shoot(x,y,freq):
    #If frequency variable is (randomly) set to a value to zero, shoot a bullet
    if freq == 0:
        # set bullet equal to the enemy bullet class
        bullet = EnemyShoot()
        # Set the bullet so it is where the enemy is
        bullet.enemytype = None
        bullet.score = None
        bullet.damage = 30
        bullet.rect.x = x
        bullet.rect.y = y
        bullet.count = 0
        bullet.counter = 0
        bullet.deathtype = 0
        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        block_bullet_list.add(bullet)

'''
def Boss_Attack1(x,y):
    bullet = Boss_1()
    # Set the bullet so it is where the enemy is
    bullet.enemytype = "BossBullet"
    bullet.score = None
    bullet.damage = 30
    bullet.rect.x = x
    bullet.rect.y = y
    bullet.count = 0
    bullet.counter = 0
    bullet.deathtype = 0
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    block_bullet_list.add(bullet)
#Function used to instalize the player sprite
'''

#Function used to create Enemy #1
def CreateBlock():
    bullet = Block()
    #Sets the score you get for killing it and speed it will travel at
    bullet.score = 1
    bullet.speed = random.randrange(1,10) / random.randrange(2,8)
    if bullet.speed < 1:
        bullet.speed = random.randrange(1,4)
    if len(block_list) > 25:
        bullet.speed *= -1
    #determines a random int from 0-4, if it is zero than it shall have the ability to shoot
    bullet.shoot = random.randrange(5)
    bullet.die = False
    bullet.enemytype = "enemy"
    bullet.count = 0
    bullet.counter = 0
    bullet.deathtype = 0
    bullet.death = []
    # Set the bullet so it is where the player is
    bullet.rect.x = random.randrange(50, screen_width - 50)
    bullet.rect.y = random.randrange(100, screen_height-250)
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    block_list.add(bullet)
    bullet = Block()

#Function used to create Enemy #2
def CreateBlock2():
    bullet = Block2()
    #Sets the score you get for killing it and speed it will travel at
    bullet.score = 2
    bullet.speed = random.randrange(1,5)
    #determines a random int from 0-4, if it is zero than it shall have the ability to shoot
    bullet.shoot = random.randrange(5)
    bullet.die = False
    bullet.enemytype = "enemy2"
    bullet.count = 0
    bullet.counter = 0
    #The death animation it will use it #3
    bullet.deathtype = 3
    bullet.death = []
    # Set the bullet so it is where the player is
    bullet.rect.x = random.randrange(50, screen_width - 50)
    bullet.rect.y = -random.randrange(1000)
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    block_list.add(bullet)
    bullet = Block2()

#Creates the "Suicide Drone" Enemy #3
def CreateEnemyDisk():
    bullet = EnemyDisk()
    #Sets speed intergers that the disk will increase to when in certain range of the player
    bullet.t1 = 5
    bullet.t2 = 4
    bullet.t3 = 3
    bullet.t4 = 1
    #sets the default x and y speed
    bullet.yspeed = 3
    bullet.xspeed = random.randrange(1,4)
    #Set the point in which the disk will charge at the player
    bullet.distance = random.randrange(1,500)
    #You get 5 points for killing it
    bullet.score = 5
    #it isnt dead! 
    bullet.die = False
    bullet.enemytype = "disk"
    bullet.count = 0
    bullet.counter = 0
    bullet.damage = 20
    bullet.deathtype = 4
    # Set the bullet so it is where the player is
    bullet.rect.x = random.randrange(screen_width)
    bullet.rect.y = -random.randrange(0,10)
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    block_list.add(bullet)
    bullet = EnemyDisk()

#Creates the balloons used in the bonus lvl
def CreateLevel():
    bullet = Balloon()
    #You get zero points for shooting one
    bullet.score = 0
    bullet.deathtype = 3
    bullet.death = []
    bullet.enemytype = "balloon"
    bullet.count = 0
    bullet.counter = 0
    # Set the bullet so it is where the player is
    bullet.rect.x = random.randrange(50, screen_width - 200)
    bullet.rect.y = random.randrange(screen_height)
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    block_list.add(bullet)
    bullet = Balloon()   
'''
def CreateBoss():
    boss = Boss()
    boss.speed = 5
    boss.counter = 0
    boss.count = 0
    boss.score = 100
    boss.Health = 100
    boss.die = False
    boss.hitxy = []
    boss.deathtype = 4
    boss.enemytype = "Boss"
    # Set the bullet so it is where the player is
    boss.rect.x = 400
    boss.rect.y = 400
    # Add the bullet to the lists
    block_list.add(boss)
    all_sprites_list.add(boss)
    boss = Boss()
'''
#--------------Power UP Creation-------------------#
#Function that creates Single Bullets  (Powerup #1)
def Power_Reg_Call():
    # Plays the sound of the shot
    RegShot.play()
    # Fire a bullet if the user clicks the mouse button
    bullet = Bullet()
    bullet.hit = False
    # Set the bullet so it is where the player is
    bullet.rect.x = rect[0]+40
    bullet.rect.y = 725
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    bullet_list.add(bullet)
    # Fire a bullet if the user clicks the mouse button
    bullet = Bullet()
##Function that creates Double Bullets Bullet  (Powerup #2)
def Power_Double_Call():
    # Plays the sound of the shot
    DoubleShot.play()
    # Fire a bullet if the user clicks the mouse button
    bullet = Bullet()
    # Set the bullet so it is where the player is
    bullet.rect.x = rect[0]+5
    bullet.rect.y = 760
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    bullet_list.add(bullet)
    # Fire a bullet if the user clicks the mouse button
    bullet = Bullet()
    # Set the bullet so it is where the player is
    bullet.rect.x = rect[0]+75
    bullet.rect.y = 760
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    bullet_list.add(bullet)
#Function that Creates the fire shot (Powerup #3)
def Power_Goto_Call():
    if fireshot.fire == 28:
        fireshot.pos = rect[0]
        bullet = Goto()
        # Plays the sound of the shot
        FireShot.play()
        # Fire a bullet if the user clicks the mouse button
        fireshot.fire = 0
        # Set the bullet so it is where the player is
        bullet.rect.x = rect[0]+40
        bullet.rect.y = 725
        # Add the bullet to the lists
        #all_sprites_list.add(bullet)
        
        # Fire a bullet if the user clicks the mouse button
#Function that creates the piercing bullets (Powerup #4)
def Power_Hard_Call():
    # Plays the sound of the shot
    PierceShot.play()
    # Fire a bullet if the user clicks the mouse button
    bullet = Hard()
    # Set the bullet so it is where the player is
    bullet.rect.x = rect[0]+40
    bullet.rect.y = 725
    # Add the bullet to the lists
    all_sprites_list.add(bullet)
    hardbullet_list.add(bullet)
    # Fire a bullet if the user clicks the mouse button
    bullet = Hard()
#--------------------------------------------------------------------------#

# Function used to handle the onscreen indicator showing the selected powerup
def Power_Select_Update():
    #Checks the type of bullet that is currently selected and draws the according box on the screen
    if Bullet_Type == "Reg":
        pygame.draw.rect(screen, GREEN, (420, 50, 30, 30), 3)
    elif Bullet_Type == "Double":
        pygame.draw.rect(screen, GREEN, (485, 50, 30, 30), 3)
    elif Bullet_Type == "Goto":
        pygame.draw.rect(screen, GREEN, (547, 50, 30, 30), 3)
    elif Bullet_Type == "Hard":
        pygame.draw.rect(screen, GREEN, (613, 50, 30, 30), 3)
    elif Bullet_Type == "AOE":
        pygame.draw.rect(screen, GREEN, (678, 50, 30, 30), 3)



# ------------------------CLASSES USED TO HANDLE ONSCREEN SPRITES-----------------#
#Class for the enemy sprites on lvl 1
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    image = pygame.image.load('spaceship1.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()

class Block2(pygame.sprite.Sprite):
    """ This class represents the block. """
    image = pygame.image.load('evilfighter.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()
'''
class Boss(pygame.sprite.Sprite):
    image = pygame.image.load('BossShip.png').convert_alpha()
    t1 = 5
    t2 = 4
    t3 = 3
    t4 = 1
    p1 = [100,100]
    p2 = [500, 300]
    p3 = [800,400]
    p4 = [300, 300]
    Attack = False
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()
    def goto(self, p):
        if self.rect.x > p[0]:
            if (self.rect.x - p[0]) >300:
                self.xspeed = -self.t1
            elif (self.rect.x - p[0]) >200:
                self.xspeed = -self.t2
            elif (self.rect.x - p[0]) > 100:
                self.xspeed = -self.t3
            elif (self.rect.x - p[0]) > 50:
                self.xspeed = -self.t4
            else:
                self.xspeed = 0 
        else:
            if (self.rect.x - p[0]) < -300:
                self.xspeed = self.t1
            elif (self.rect.x - p[0]) < -200:
                self.xspeed = self.t2
            elif (self.rect.x - p[0]) < -100:
                self.xspeed = self.t3
            elif (self.rect.x - p[0]) < -50:
                self.xspeed = self.t4
            else:
                self.xspeed = 0
        if self.rect.y > p[1]:
            if (self.rect.y - p[1]) >300:
                self.yspeed = -self.t1
            elif (self.rect.y - p[1]) >200:
                self.yspeed = -self.t2
            elif (self.rect.y - p[1]) > 100:
                self.yspeed = -self.t3
            elif (self.rect.y - p[1]) > 50:
                self.yspeed = -self.t4
            else:
                self.yspeed = 0 
        else:
            if (self.rect.y - p[1]) < -300:
                self.yspeed = self.t1
            elif (self.rect.y - p[1]) < -200:
                self.yspeed = self.t2
            elif (self.rect.y - p[1]) < -100:
                self.yspeed = self.t3
            elif (self.rect.y - p[1]) < -50:
                self.yspeed = self.t4
            else:
                self.xspeed = 0 
        print(p[1])
            
    def update(self):
        if self.counter == 0:
            self.goto(self.p1)
            if self.rect.x >= self.p1[0] -50 and self.rect.x <= self.p1[0] +50:
                if self.rect.y >= self.p1[1] -50 and self.rect.y <= self.p1[1] +50:
                    self.Attack = True
                    self.counter += 1
        if self.counter == 1:
            self.goto(self.p2)
            if self.rect.x >= self.p2[0] -50 and self.rect.x <= self.p2[0] +50:
                if self.rect.y >= self.p2[1] -50 and self.rect.y <= self.p2[1] +50:
                    self.Attack = True
                    self.counter += 1
        if self.counter == 2:
            self.goto(self.p3)
            if self.rect.x >= self.p3[0] -50 and self.rect.x <= self.p3[0] +50:
                if self.rect.y >= self.p3[1] -50 and self.rect.y <= self.p3[1] +50:
                    self.Attack = True
                    self.counter += 1
        if self.counter == 3:
            self.goto(self.p4)
            if self.rect.x >= self.p4[0] -50 and self.rect.x <= self.p4[0] +50:
                if self.rect.y >= self.p4[1] -50 and self.rect.y <= self.p4[1] +50:
                    self.Attack = True
                    self.counter = 0        
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
'''       
    
#Class used to handle the player sprite
player_rectx = rect[0]
player_recty = 780

class Balloon(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    image = pygame.image.load('balloon.gif').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()
        
    def die(self):
        """ Move the bullet. """
        CreatePower(random.randrange(1,3), random.randrange(2,5), self.rect.x+20, self.rect.y+20, self.rect.x-20, self.rect.y-20)
        CreatePower(random.randrange(1,3), random.randrange(2,5), self.rect.x+20, self.rect.y+20, self.rect.x-20, self.rect.y-20)
        
#Class used for the Disk enemy "Suicide Drone"
class EnemyDisk(pygame.sprite.Sprite):
    image = pygame.image.load('qSpaceDisk.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()
    def update(self):
        #When the Disk is out of range of the player it will decend at a speed of 2 down
        self.yspeed = 2
        #Will go left and right until the sprite passes the random threshold set in creation
        if self.rect.y < self.distance:
            self.rect.x += self.xspeed
            if self.rect.x > screen_width -50 or self.rect.x < 0:
                self.rect.y += 50
                self.xspeed*= -1
        #If it passes the threshold it will head toward the player
        else:
            #If the x value is greater than the players it will decrease the x value
            if self.rect.x > rect[0]:
                if (self.rect.x - rect[0]) >300:
                    self.xspeed = -self.t1*random.randrange(1,2)
                elif (self.rect.x - rect[0]) >200:
                    self.xspeed = -self.t2*random.randrange(1,2)
                elif (self.rect.x - rect[0]) > 100:
                    self.xspeed = -self.t3*random.randrange(1,2)
                else:
                    self.xspeed = -self.t4*random.randrange(1,2)
            #If the x value is less than the players it will increase the x value
            else:
                if (self.rect.x - rect[0]) < -200:
                    self.xspeed = self.t1*random.randrange(1,2)
                elif (self.rect.x - rect[0]) < -100:
                    self.xspeed = self.t2*random.randrange(1,2)
                elif (self.rect.x - rect[0]) < -50:
                    self.xspeed = self.t3*random.randrange(1,2)
                else:
                    self.xspeed = self.t4*random.randrange(1,2)
            #If the x value is greater than the players it will check the y values
            if (self.rect.x - rect[0]) > -300 and (self.rect.x - rect[0]) < 300:
                #Increases the yspeed values in intervals 
                if (self.rect.y - 680) > 300:
                    self.yspeed = self.t4
                elif (self.rect.y - 680) >200:
                    self.yspeed = self.t3
                elif (self.rect.y - 680) > 100:
                    self.yspeed = self.t2
                else:
                    self.yspeed = self.t1
            #Adds the yand x speed to the y and x positions 
            self.rect.x += self.xspeed
            self.rect.y += self.yspeed
'''  
class Boss_1(pygame.sprite.Sprite):
    image = pygame.image.load('Boss_Balls.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()
    def update(self):
        """ Move the bullet. """
        if self.rect.x > rect[0]:
            if (self.rect.x - rect[0]) >300:
                self.xspeed = -self.t1*random.randrange(1,2)
            elif (self.rect.x - rect[0]) >200:
                self.xspeed = -self.t2*random.randrange(1,2)
            elif (self.rect.x - rect[0]) > 100:
                self.xspeed = -self.t3*random.randrange(1,2)
            else:
                self.xspeed = -self.t4*random.randrange(1,2)
        else:
            if (self.rect.x - rect[0]) < -200:
                self.xspeed = self.t1*random.randrange(1,2)
            elif (self.rect.x - rect[0]) < -100:
                self.xspeed = self.t2*random.randrange(1,2)
            elif (self.rect.x - rect[0]) < -50:
                self.xspeed = self.t3*random.randrange(1,2)
            else:
                self.xspeed = self.t4*random.randrange(1,2)
        if (self.rect.x - rect[0]) > -300 and (self.rect.x - rect[0]) < 300:
            if (self.rect.y - 680) > 300:
                self.yspeed = self.t4
            elif (self.rect.y - 680) >200:
                self.yspeed = self.t3
            elif (self.rect.y - 680) > 100:
                self.yspeed = self.t2
            else:
                self.yspeed = self.t1
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
'''
        

#Class used to handle the player's main bullets (Powerup 1)
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    image = pygame.image.load('bullet.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 5
        
#Class used to handle the Enemy's main bullets        
class EnemyShoot(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    image = pygame.image.load('bullet3.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
 
        self.rect = self.image.get_rect()
        
    def update(self):
        """ Move the bullet. """
        self.rect.y += 5
#Class used to handle the player's piercing bullets (Powerup 4)
class Hard(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    image = pygame.image.load('bullet2.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 5 
#Class used to handle the player's fireblast (Powerup 3) 
class Goto(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    count = 0
    image = pygame.image.load('hit.gif').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.rect = fireball[1].get_rect()
    def shoot(self):
        if fireshot.fire <= 27:
            screen.blit(pygame.transform.rotate(fireball[fireshot.fire],90), [rect[0]-62, 340]),90, [rect[0]-62, 340]
            fireshot.fire += 1     

#Creates all variables pertaining to the fireblast animation/sprite
fireshot = Goto()
fireshot.fireframe = 0
fireshot.firedraw = 0
fireshot.fire = 28
fireshot.fireball = fireball

#--------------------CLASSES USED Directally FOR DRAWING THE ONSCREEN ICONS-------------------# 
class Power2(pygame.sprite.Sprite):
    """ This class represents the block. """
    image = pygame.image.load('doubleShot.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
class Power3(pygame.sprite.Sprite):
    """ This class represents the block. """
    image = pygame.image.load('fireShot.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
class Power4(pygame.sprite.Sprite):
    """ This class represents the block. """
    image = pygame.image.load('piercingShot.png').convert_alpha()
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
#-------------------------------------------------------------------------------------------#
#Graphics Class is used to draw all non-sprite objects to the screen 
class Graphics():
    #Creates all atributes used in Graphics Class
    #Loads all images used in Graphics Class
    Header = pygame.image.load('headerGui.png').convert_alpha()
    GameOver = pygame.image.load('loseScreen.png').convert()
    GameOverW = pygame.image.load('WinScreen.png').convert()
    crosshair =  pygame.image.load('crosshair.png').convert_alpha()
    done = False
    def GUI(self):
        #If the game is not over, draw this: 
        if gameover[0] == False:
            #Defines the Width of the health and focus bars
            Hwidth = (player_Health/100) * 152
            Swidth = (ShieldBar/100) * 152
            #Blits the main header GUI on the top of the screen 
            screen.blit(self.Header, [0,0])
            #Draws the health and focus bars
            pygame.draw.rect(screen, RED, [24,48,Hwidth,18], 0)
            pygame.draw.rect(screen,GREEN, [210,48,Swidth,18],0)
            #Blits the aiming crosshair ontop of the mouse
            screen.blit(self.crosshair, [player_rectx-13,rect[1]])
            #Highlights the selected power
            Power_Select_Update()
            #Renders the varius texts 
            scoreText = font.render("" + str(score), True, WHITE)
            Amo2Text = font2.render("" + str(Power2_Amo), True, WHITE)
            Amo3Text = font2.render("" + str(Power3_Amo), True, WHITE)
            Amo4Text = font2.render("" + str(Power4_Amo), True, WHITE)
            #Blits the varius texts onto the screen
            screen.blit(scoreText, [900, 30])
            screen.blit(Amo2Text, [490, 80])
            screen.blit(Amo3Text, [560, 80])
            screen.blit(Amo4Text, [625, 80])
        #If the game is over than do this:
        else:
            #If You lost:
            if gameover[1] == "Lose":
                
                self.GameOver = pygame.transform.scale(self.GameOver, [screen_width, screen_height])
                while not self.done:
                    screen.blit(self.GameOver, [0,0])
                    scoreText = font.render("" + str(score), True, WHITE)
                    #Blits the varius texts onto the screen
                    screen.blit(scoreText, [550, 390])
                    reasonText = font.render("" + str(reason), True, WHITE)
                    screen.blit(reasonText, [300, 500])
                    for event in pygame.event.get():
                        #Checks to see if user presses a key
                        if event.type == pygame.KEYDOWN:
                            self.done = True
                    pygame.display.flip()
                #Blits the GameOver Page onto the screen
                #self.GameOver = pygame.transform.scale(self.GameOver, [screen_width, screen_height])
                #screen.blit(self.GameOver, [0,0])
                #Prints your final score
                #scoreText = font.render("" + str(score), True, WHITE)
                #screen.blit(scoreText, [550, 390])
            #If you won: 
            elif gameover[1] == "Win":
                #Blits the GameOver Page onto the screen
                self.GameOverW = pygame.transform.scale(self.GameOverW, [screen_width, screen_height])
                screen.blit(self.GameOverW, [0,0])
                #Prints your final score
                scoreText = font.render("" + str(score), True, WHITE)
                screen.blit(scoreText, [550, 390])
            #Prints your reason for ending the game onto the screen    

#Function that clears the screen of all sprites 
def cleanscreen():
    #clears the block List
    for block in block_list:
        block_list.remove(block)
        all_sprites_list.remove(block)
    #clears the piercing bullet List
    for block in hardbullet_list:
        hardbullet_list.remove(block)
        all_sprites_list.remove(block)
    #clears the block's bullet List
    for block in block_bullet_list:
        block_bullet_list.remove(block)
        all_sprites_list.remove(block)
    #clears the animation List
    for block in Animate_list:
        Animate_list.remove(block)
        all_sprites_list.remove(block)
    #clears the icon List
    for block in Icon_list:
        Icon_list.remove(block)
        all_sprites_list.remove(block) 
    

#Function for printing the Mission report brfore eahc mission
def missionreport(pic,done):
    while not done:
        screen.blit(pic, [0,0])
        scoreText = font.render("" + str(score), True, BLACK)
        #Blits the varius texts onto the screen
        screen.blit(scoreText, [900, 30])
        for event in pygame.event.get():
            #Checks to see if user presses a key
            if event.type == pygame.KEYDOWN:
                done = True
        pygame.display.flip()

#function For printing the Winner screen when game is won! 
def End(win, done):
    while not done:
        screen.blit(pic, [0,0])
        scoreText = font.render("" + str(score), True, BLACK)
        #Blits the varius texts onto the screen
        screen.blit(scoreText, [900, 30])
        for event in pygame.event.get():
            #Checks to see if user presses a key
            if event.type == pygame.KEYDOWN:
                done = True
        pygame.display.flip()
    
#function that blits the ammount of reinforcemnts to the screen
def reinforcements(amount):
    text = font.render(str(amount) + " Reinforcements Arrived!", True, WHITE)
    screen.blit(text, [550, 390])

# --- Level Functions --- #
#Function that instalises level one 
def Levelone():
    Mission = pygame.image.load('Mission1.png').convert_alpha()
    missionreport(Mission,False)
    # Create Type 2 Powerups:
    CreatePower(random.randrange(5), 2, screen_width-10, screen_height-200, 50, 100)
    #Create Type 3 Powerups:
    CreatePower(random.randrange(3), 3, screen_width-10, screen_height-200, 50, 100)
    #Create Type 4 Powerups
    CreatePower(random.randrange(5), 4, screen_width-10, screen_height-200, 50, 100)
    #Creates enemys
    for i in range(50):
        CreateBlock()
    for i in range(3):
        CreateEnemyDisk()

#Function that instalises level two 
def Leveltwo():
    Mission = pygame.image.load('Mission2.png').convert_alpha()
    missionreport(Mission,False)
    for i in range(10):
        CreateEnemyDisk()
        CreateBlock2()
#Function that instalises the bonus level
def LevelBonus():
    Mission = pygame.image.load('MissionBonus.png').convert_alpha()
    missionreport(Mission,False)
    for i in range(20):
        CreateLevel()
'''
def LevelBoss():
    Mission = pygame.image.load('Mission1.png').convert_alpha()
    missionreport(Mission,False)
    CreateBoss()    
'''
#Starts the First Level
Levelone()
Level = 1

#Sets some variables used for the time
frame_count = 0
frame_rate = 60
start_time = 90



#Disables the mouse visibility 
pygame.mouse.set_visible(False)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    #If you loose it will exit the loop
    if gameover[1] == "Lose":
        done = True
    # --- Event Processing
    for event in pygame.event.get():
        #If the user chooses to exit the game, then done becomes true
        if event.type == pygame.QUIT:
            done = True
            gamedone = True
        #Checks to see if user presses a key
        elif event.type == pygame.KEYDOWN:
            #Sets the bullet type to Regular when 1 is pressed
            if event.key == pygame.K_1:
                Bullet_Type = "Reg"
            #Sets the bullet type to Double when 2 is pressed
            elif event.key == pygame.K_2:
                Bullet_Type = "Double"
            #Sets the bullet type to Goto (fireshot) when 3 is pressed
            elif event.key == pygame.K_3:
                Bullet_Type = "Goto"
            #Sets the bullet type to Hard (peircing) when 4 is pressed
            elif event.key == pygame.K_4:
                Bullet_Type = "Hard"
            #Slows down the gamespeed when space is pressed (focus mode)
            elif event.key == pygame.K_SPACE:
                #Will only allow slow mo when the focus bar is at 100 percent
                if ShieldBar == 100:
                    GlobalSpeed = 30
                    Slowmo.play()
            #If key is x and the user is hovering over an icon... Collect that icon
            elif event.key == pygame.K_x:
                #Checks each x and y value for each icon in the icon_list
                for icon in Icon_list:
                    if icon.rect.x < rect[0]+41 and icon.rect.x+30 >rect[0]+41:
                        if icon.rect.y < rect[1]+52 and icon.rect.y+30 > rect[1]+52:
                            #if the icon being hovered on is #2 than reduce that power's ammo and play the powerup sound
                            if icon.typ == 2:
                                Power2_Amo += 5
                            elif icon.typ == 3:
                                Power3_Amo += 2
                            elif icon.typ == 4:
                                Power4_Amo += 5
                            Powerup.play()
                            #Remove the icon from the icon list and all sprite lists
                            Icon_list.remove(icon)
                            all_sprites_list.remove(icon)

        # Backspace to go back to menu --> Only usable when you win/lose
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_BACKSPACE and gameover[0] == True:
               done = True

        #Checks if the user pressed the left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #As long as the player's shooting timer is still in effect (Shoot) nothing will run
            if Shoot == False:
                #If the selected bullet type is Goto (3):
                if Bullet_Type == "Goto":
                    #If the player doesnt have ammo set the "out of ammo" text counter to 0
                    if Power3_Amo <= 0:
                        Text_Count = 0
                    #If they do have ammo Shoot the bullet and subtract from their ammo
                    else:
                        Power3_Amo -= 1
                        Shoot = True
                        Power_Goto_Call()
                #If the selected bullet type is Reg (1):
                elif Bullet_Type == "Reg":
                    Shoot = True
                    Power_Reg_Call()
                #If the selected bullet type is Double (2):
                elif Bullet_Type == "Double":
                    #If the player doesnt have ammo set the "out of ammo" text counter to 0
                    if Power2_Amo <= 0:
                        Text_Count = 0
                    #If they do have ammo Shoot the bullet and subtract from their ammo
                    else:
                        Power2_Amo -= 1
                        Shoot = True
                        Power_Double_Call()
                #If the selected bullet type is Hard (4):
                elif Bullet_Type == "Hard":
                    #If the player doesnt have ammo set the "out of ammo" text counter to 0
                    if Power4_Amo <= 0:
                        Text_Count = 0
                    #If they do have ammo Shoot the bullet and subtract from their ammo
                    else:
                        Power4_Amo -= 1
                        Shoot = True
                        Power_Hard_Call()
    #set rect equal to the mouse position
    rect = pygame.mouse.get_pos()
    # ----------------------------MAIN GAME LOGIC / HIT DETECTION--------------------------- #
    #Checks each bullet in the enemy bullet list
    for bullet in block_bullet_list:
        #If the bullet contacts the player sprite remove it and subtract from player health
        if bullet.rect.x > rect[0] and bullet.rect.x < rect[0]+80:
            if bullet.rect.y > 680 and bullet.rect.y < 750:
                bullet.deathtype = 1
                player_Health -= bullet.damage
                Animate_list.add(bullet)
                block_bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
        #If the bullet goes below the screen, remove the bullet
        if bullet.rect.y < -10:
            block_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        
    #Checks the enemies in the enemy sprite list
    for block in block_list:
        #Checks if the enemytype is the disk
        if block.enemytype == "disk":
            #Updates each disk's position
            block.update()
            #Checks detection against the player sprite
            if block.rect.x > rect[0]-50 and block.rect.x < rect[0]+80 and block.rect.y > 600 and block.rect.y < 700:
                #Does damage tot he player
                player_Health -= block.damage
                block.deathtype = 3
                block.score = None
                block.damage = 20
                #Removes the block from the sprite lists and adds it to the animation list
                Animate_list.add(block)
                block_list.remove(block)
                all_sprites_list.remove(block)
            #Removes the block from the sprite lists if it passes the screen
            if block.rect.y > screen_height:
                    block_list.remove(block)
                    all_sprites_list.remove(block)
            #Checks if the block has entered the fireball 
            if fireshot.fire > 0 and fireshot.fire < 28:
                if block.rect.x > rect[0]-50 and block.rect.x < rect[0] +80 and block.rect.y > 300 and block.rect.y < 630:
                    block.deathtype = 3
                    #Removes the block from the sprite lists and adds it to the animation list
                    Animate_list.add(block)
                    block_list.remove(block)
                    all_sprites_list.remove(block)                
                    
        if Level == 1 and block.enemytype != "disk":
            #If the enemy hits the side of the screen change direction by a multiple of -1.1 and randomly add to the y position
            if block.rect.x > screen_width-10 or block.rect.x < 0:
                block.speed *= - 1.1 
                block.rect.y += random.randrange(50)
            #Increase each block's x positon by its random specified speed
            block.rect.x += block.speed
            #Allows one in five of the enemy sprites to shoot, as only one in five have a shoot value of zero,
            # and it will only let them shoot if the y position is above 500
            if block.shoot == 0 and block.rect.y < 500:
                Enemy_Shoot(block.rect.x,block.rect.y,random.randrange(100))
            #If the enemy sprite collides with the player sprite, end the game. 
            if (block.rect.x -rect[0]) < 75 and (block.rect.x -rect[0]) > -50 and block.rect.y > 700:
                player_Health = -1
                ContactDeath = True
            #Checks for enemy collision with the fireshot animation 
            if fireshot.fire > 0 and fireshot.fire < 28:
                if (block.rect.x -rect[0]) < 75 and (block.rect.x -rect[0]) > -50 and block.rect.y > 300:
                    block.deathtype = 2
                    Animate_list.add(block)
                    block_list.remove(block)
                    all_sprites_list.remove(block)
        #Checks if the level is two and the enemytype isnt disk
        elif Level == 2 and block.enemytype != "disk":
            #Resets position if it passes the screen 
            if block.rect.y > screen_width:
                block.rect.y = 0
                block.rect.x = random.randrange(screen_width)
            #Constanly increasing the speed by.001 plus the blockspeed 
            block.rect.y += block.speed+1
            block.speed += .001
            #Checks for collisio with the player
            if block.rect.x > rect[0]-70 and block.rect.x < rect[0]+80 and block.rect.y > 600 and block.rect.y < 730:
                #Decreases playerhealth
                player_Health -= 20
                block.deathtype = 3
                #removes the enemy from the sprite lists and adds it to the animation list
                Animate_list.add(block)
                block_list.remove(block)
                all_sprites_list.remove(block)
            #Checks if the emeny touched the fireball        
            if fireshot.fire > 0 and fireshot.fire < 28:
                if block.rect.x > rect[0]-70 and block.rect.x < rect[0] +80 and block.rect.y > 300 and block.rect.y < 630:
                    block.deathtype = 3
                    #removes the fireball form the sprite lists and adds to animation list
                    Animate_list.add(block)
                    block_list.remove(block)
                    all_sprites_list.remove(block)
        '''elif Level == "Boss" and block.enemytype == "Boss":
            if block.attack == True:
                block.attacktyp = random.randrange(1,5)
                if block.attacktyp == 0:
        '''            
                    
                    
            
           
            
    #Checks the bullets in the player bullet list
    for bullet in bullet_list:
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            '''
            if block.enemytype == "Boss":
                block_list.add(block)
                all_sprites_list.add(block)
                block.hitxy = [bullet.rect.x,bullet.rect.y]
                block.deathtype = 4
                Animate_list.add(block)
            '''
            block.deathtype = 1
            Animate_list.add(block)
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
    #Checks the bullets in the hard bullet list (piercing) 
    for bullet in hardbullet_list:
        # See if it hit a block, remove the block, but dont remove the bullet
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        for block in block_hit_list:
            block.deathtype = 1
            Animate_list.add(block)
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            hardbullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
           
    # Call the update() method on all the sprites
    screen.blit(backgroundImage,[0,0])
    
    # --- Draw a frame 
    if fireshot.fire <= 27:
        pygame.mouse.set_pos([fireshot.pos, 380])
        Goto().shoot()
 
    # Draw all the spites to the screen
    all_sprites_list.draw(screen)
    #Update the graphics on the screen
    Graphics().GUI()

    #Animates the Enemy Death's 
    if len(Animate_list) >0:
        #For each item in the animate list... animate
        for bullet in Animate_list:
            #Checks the deathtype and blits the according animation
            if bullet.deathtype == 1:
                screen.blit(EnemyDeath[bullet.count], (bullet.rect.x,bullet.rect.y))
            elif bullet.deathtype == 2:
                screen.blit(EnemyDeath2[bullet.count], (bullet.rect.x,bullet.rect.y))
            elif bullet.deathtype == 3:
                screen.blit(EnemyDeath3[bullet.count], (bullet.rect.x-50,bullet.rect.y))
            elif bullet.deathtype == 4:
                screen.blit(EnemyDeath5[bullet.count], (bullet.hitxy[0]-100,bullet.rect.y))
            #If there is no specidied score it must be damage, notify of damage, if not it is points, notify of points 
            if bullet.score != None:
                text = "+ " + str(bullet.score) + " point(s)"
            else:
                text = "- " + str(bullet.damage) + " damage"
            #Blits the added score to the screen
            AddScore = font2.render(text, True, WHITE)
            screen.blit(AddScore, [bullet.rect.x, bullet.rect.y])
            #If it is a balloon remove it, and put the icons in its place
            if bullet.enemytype == "balloon" and bullet.counter > 40:
                bullet.die()
                bullet.enemytype = None
                Animate_list.remove(bullet)
            # Add to the counter
            bullet.counter += 1
            #Add the count(frame) every 5 counters
            if bullet.counter % 5 == 0:
                bullet.count += 1
                #If the death type is 1 stop at count(frame) 13
                if bullet.deathtype == 1:
                    if bullet.count > 13:
                        if bullet.score != None:
                            score += bullet.score
                        bullet.count = 0
                        Animate_list.remove(bullet)
                #If the death type is 2 stop at count(frame) 9
                elif bullet.deathtype == 2:
                    if bullet.count >9:
                        if bullet.score != None:
                            score += bullet.score
                        bullet.count = 0
                        Animate_list.remove(bullet)
                #If the death type is 3 stop at count(frame) 9
                elif bullet.deathtype == 3:
                    if bullet.count >9:
                        if bullet.score != None:
                            score += bullet.score
                        bullet.count = 0
                        Animate_list.remove(bullet)
                #If the death type is 4 stop at count(frame) 16
                elif bullet.deathtype == 4:
                    if bullet.count >16:
                        if bullet.score != None:
                            score += bullet.score
                        block.Health -= 10
                        bullet.count = 0
                        Animate_list.remove(bullet)
    #Update the position of all sprites                
    all_sprites_list.update()
    #-----Controls the Slowmo Mode----------#
    #While slowmo is enabled take away from the shieldbar size and add to the counter
    if GlobalSpeed == 30:
        ShieldBar -= .8
        GlobalSpeed_Counter += .8
        #When the counter passes 100, it is reset and framerate is setback to 60
        if GlobalSpeed_Counter > 100:
            GlobalSpeed_Counter=0
            GlobalSpeed = 61
            ShieldBar == 0
    #Controls the recovery of the Focus bar after slowmo
    else:
        GlobalSpeed_Counter2 += 1
        #After a period of time has elapsed after the slowmo finishes, begin bar regeneration 
        if GlobalSpeed_Counter2 > 100:
            ShieldBar += .2
            #Reset GlobalSpeed Counter #3 when GlobalSpeed is 61:
            # This makes it so that global speed is only reset once every full restore
            if GlobalSpeed == 61:
                GlobalSpeed_Counter3 = 0
            if ShieldBar > 100:
                GlobalSpeed = 60
                ShieldBar = 100
                GlobalSpeed_Counter2 = 0
    #If the shieldbar has reduced below zero, set it to 1 
    if ShieldBar < 0:
       ShieldBar = 1

    #If the Focus bar is full and the Global Counter #3 is less than 120:
    if ShieldBar == 100 and GlobalSpeed_Counter3 < 120:
        #Blits the "Focus Restored" Text onto the screen
        screen.blit(SlowmoText, [220, 100])
        GlobalSpeed_Counter3 += 1
        
        

    #If the text counter for the no ammo text is below 50, blit the warning to the screen
    if Text_Count < 50:
        screen.blit(AmoText, [400, 400])
        Text_Count += 1

    #Checks to see if the player's health is low and the game is not done as well as if the counter that controls draw time is less than 25
    if player_Health < 25 and Lowhealth_Counter < 25 and gameover[0] == False:
        #Blits the Low Health message to the screen
        screen.blit(LowhealthText, [20, 100])
        Lowhealth_Counter+=1
    else:
        Lowhealth_Counter += 1
        #Resets the text counter back to zero so it may be used again
        if Lowhealth_Counter > 50:
            Lowhealth_Counter = 0

        
    #Controls the timer between shots#
    if Shoot == True:
        Shooting_Counter += 1
        #After 20 frames have elapsed allow player to shoot again
        if Shooting_Counter  > 20:
            Shooting_Counter = 0
            Shoot = False

    # --- Timer going up ---

    frame_count += 1
    # Calculate total seconds
    total_seconds = frame_count // GlobalSpeed
     
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
     
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
     
    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    if gameover[0] != True:
        # Blit to the screen
        text = font2.render(output_string, True, WHITE)
        screen.blit(text, [790, 80])

    #Checks if player health is zero, if it is, it sets the gameover list to True and Lose and gives the according reason for loss   
    if player_Health < 0:
        for block in block_list:
            block_list.remove(block)
            all_sprites_list.remove(block)
        gameover= [True, "Lose"]
        if ContactDeath == True:
            reason = "Your ship crashed into the enemy!"
        else:
            reason = "Your ship has been destroyed by enemy fire!"
    #Checks no more enemies are list, if there arent, it sets the gameover list to True and Win and gives the according reason for Win 
    if gameover != [True, "Lose"]:
        #Spawning waves for Level Two 
        if Level == 2:
            #After 10, 30 and 60 seconds spawn 7  disks and notify the user
            if total_seconds == 10 or total_seconds == 30 or total_seconds == 60:
                spawncounter += 1
                if spawncounter < 1000:
                    reinforcements(7)
                if spawncounter < 8:
                    CreateEnemyDisk()
            #After 20 seconds, create 30 Enemy#2 and notify the user
            if total_seconds == 20:
                if spawncounter < 31:
                    CreateBlock2()
                spawncounter += 1
                if spawncounter < 1000:
                    reinforcements(30)
            #After 50 seconds, create 50 Enemy#2 and notify the user
            if total_seconds == 50:
                if spawncounter < 51:
                    CreateBlock2()
                spawncounter += 1
                if spawncounter < 1000:
                    reinforcements(50)
            #At 19, 29. 49 and 59 seconds reset the spawning counter (used for creating the waves and controling notify times
            if total_seconds == 19 or total_seconds == 29 or total_seconds == 49 or total_seconds == 59:
                spawncounter = 0
        #if its a bonus level print the time left in the level
        if Level == "+":
            text = font.render(str(-(seconds -10)) + " Seconds Left", True, WHITE)
            screen.blit(text, [450, 200])
                            
        #When Level 1 is complete:            
        if len(block_list) == 0 and Level == 1:
            #Set the level to bonus and restore the health halfway
            Level = "+"
            if player_Health < 50:
                player_Health = 50
            cleanscreen()
            #Refresh Ammo supplies
            Power2_Amo += 10
            Power3_Amo += 2
            Power4_Amo += 5
            frame_count = 0
            #set background to the bonus baackfground 
            backgroundImage = pygame.image.load('Bonus.png').convert()
            #If the user beat the time bonus give them 100 points 
            if total_seconds <= 30:
                score += 100
            #Reset time and call the next level
            total_seconds = 0
            LevelBonus()
        #If Level 2 is complete
        elif len(block_list) == 0 and Level == 2 and total_seconds > 60:
            Level = None
            #If the user beat the time bonus give em points
            if total_seconds < 90:
                score += 500
            #Clear the screen and reset time
            cleanscreen()
            total_seconds = 0
            frame_count = 0
            #Print the winning screen and exit
            missionreport(winner,False)
            done = True
            
        #If the user beat the bonus level:
        elif len(block_list) == 0 and Level == "+" or total_seconds > 10 and Level == "+":
            #Set level to two 
            Level = 2
            #Clear the screen and reset time
            cleanscreen()
            total_seconds = 0
            frame_count = 0
            #set background to space.jpg and call lvl2 
            backgroundImage = pygame.image.load('space.jpg').convert()
            Leveltwo()
            
    rect = pygame.mouse.get_pos()
    # Set the player x position to the mouse x position
    player_rectx = rect[0]
    
    #------------------------------------------------------# 
    #Logic for animating the player 
    player_count+=1
    if player_count % 4 == 0:
        player_Counter += 1
    if player_Counter >3:
        player_Counter = 0
    if gameover[0] != True:
        screen.blit(PlayerSprite[player_Counter],[player_rectx,680])
    #------------------------------------------------------# 
     
    #Updates the screen
    pygame.display.flip()
    # --- Limit frames to specified amount (30 in slowmo and 60 normal)    
    clock.tick(GlobalSpeed)
pygame.quit()


