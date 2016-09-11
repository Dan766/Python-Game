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
Rev 2.3
June 5, 2014
'''
#Imports the Menu program which is used for all the menu interaction
import Menu
#Imports the gameover variable from ShootGame 
from ShootGame import gameover
#Imports the sys module used for deleting module data
import sys
#Imports the ShootGame Module which is used for all the main game code
import ShootGame
#Cycles through the Menu and ShootGame programs until gameover is True
while ShootGame.gamedone == False:
    del sys.modules['ShootGame']
    del sys.modules['Menu']
    import Menu
    import ShootGame
    

