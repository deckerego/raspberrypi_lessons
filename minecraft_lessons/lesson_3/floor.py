import mcpi.minecraft as minecraft
import mcpi.block as block

running_game = minecraft.Minecraft.create()

running_game.postToChat("Diamonds are forever!")

playerPosition = running_game.player.getTilePos()
running_game.setBlocks(
	playerPosition.x - 1, 
	playerPosition.y - 25, 
	playerPosition.z - 25,
	playerPosition.x - 1,
	playerPosition.y + 25,
	playerPosition.z + 25,
	block.NETHER_REACTOR_CORE)