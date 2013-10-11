import mcpi.minecraft as minecraft
import mcpi.block as block

running_game = minecraft.Minecraft.create()

running_game.postToChat("Going up!")

playerPosition = running_game.player.getPos()
running_game.player.setPos(playerPosition.x - 100, playerPosition.y -17, playerPosition.z)
