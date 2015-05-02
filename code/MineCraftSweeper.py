###TeCoEd###
###MineCraft Sweeper###

import random
import time
from mcpi import minecraft
mc = minecraft.Minecraft.create()

global bomb
bomb = random.randrange(0, 11, 1)
print bomb

###Creates the Board###
mc.postToChat("Welcome to Minecraft MineSweeper")
x, y, z = mc.player.getPos()
mc.setBlocks(x, y-1, z, x+20, y-1, z+20, 58)

###Places the bomb###
bomb_x = int(x+bomb)
bomb_y = int(y-1)
bomb_z = int(z+bomb)

print bomb_x, bomb_y, bomb_z ###test
mc.setBlock(bomb_x, bomb_y, bomb_z,58)

score = 0

mc.postToChat("Score is "+str(score))
#test = mc.setBlock(x + bomb, y-1, z + bomb, 46,1)
time.sleep(10)
while True:  ###TEST IF YOU STAND ON THE BLOCK
    
    x1, y1, z1 = mc.player.getTilePos()
    #print x1, y1, z1 ###test
    time.sleep(0.1)
    score = score + 1
    if (x1, y1-1, z1) == (bomb_x, bomb_y, bomb_z):
        mc.setBlocks(x-5, y+1, z-5, x+5, y+2, z+5, 10) ##CHANGE TO WATER?
        print "GAME OVER"
        mc.postToChat("G A M E  O V E R")
        mc.postToChat("Score is "+str(score))
        break
    else:
        mc.setBlock(x1, y1-1, z1, 41)
        
        
        
    
mc.postToChat("GAME OVER")         
