"""World 1-1."""

import pygame
import engine
import lostlevels
import lostlevels.scenes
import lostlevels.sprites

from .. import levelgenerator

# Define the level data for this level's main section.
class Level11_main(levelgenerator.LevelData):
    # Create the level data for the current section.
    def __init__(self, engine, level, player_offset, biome):
        # Call the LevelData constructor.
        super().__init__(engine, level, player_offset, biome)

        # Play the level music. 
        level.play_music(biome)

# Return a path to the image preview of this level.
def get_preview():
    return "engine/assets/missing.png"

# Generate the level data for this level.
def load_leveldata(engine: engine.LLEngine, level: lostlevels.scenes.Level, section):
    # Is this the main section?
    if section == "main":
        # Create the level generator and level data for this section.
        gen = levelgenerator.LevelGenerator(engine, level, "overground")
        data = Level11_main(engine, level, pygame.math.Vector2(32, -358), "overground")

        # Create the main ground.
        gen.generate_ground(pygame.math.Vector2(0, -416), 69, 2)
        gen.generate_ground(pygame.math.Vector2(2272, -416), 15, 2)
        gen.generate_ground(pygame.math.Vector2(2848, -416), 64, 2)
        gen.generate_ground(pygame.math.Vector2(4960, -416), 80, 2)

        # Create the power-up blocks.
        gen.generate_powerup_block(pygame.math.Vector2(512, -288))
        gen.generate_powerup_block(pygame.math.Vector2(672, -288))
        gen.generate_powerup_block(pygame.math.Vector2(736, -288))
        gen.generate_powerup_block(pygame.math.Vector2(704, -160))
        gen.generate_powerup_block(pygame.math.Vector2(2048, -256), draw = False)
        gen.generate_powerup_block(pygame.math.Vector2(2496, -288))
        gen.generate_powerup_block(pygame.math.Vector2(3008, -160))
        gen.generate_powerup_block(pygame.math.Vector2(3008, -288), decoy = True)
        gen.generate_powerup_block(pygame.math.Vector2(3232, -288), decoy = True)
        gen.generate_powerup_block(pygame.math.Vector2(3392, -288))
        gen.generate_powerup_block(pygame.math.Vector2(3488, -288))
        gen.generate_powerup_block(pygame.math.Vector2(3584, -288))
        gen.generate_powerup_block(pygame.math.Vector2(3488, -160))
        gen.generate_powerup_block(pygame.math.Vector2(4128, -160), 2)
        gen.generate_powerup_block(pygame.math.Vector2(5440, -288))

        # Create the destructible blocks.
        gen.generate_destructible(pygame.math.Vector2(640, -288))
        gen.generate_destructible(pygame.math.Vector2(704, -288))
        gen.generate_destructible(pygame.math.Vector2(768, -288))
        gen.generate_destructible(pygame.math.Vector2(2464, -288))
        gen.generate_destructible(pygame.math.Vector2(2528, -288))
        gen.generate_destructible(pygame.math.Vector2(2560, -160), 8)
        gen.generate_destructible(pygame.math.Vector2(2912, -160), 3)
        gen.generate_destructible(pygame.math.Vector2(3200, -288))
        gen.generate_destructible(pygame.math.Vector2(3776, -288))
        gen.generate_destructible(pygame.math.Vector2(3872, -160), 3)
        gen.generate_destructible(pygame.math.Vector2(4096, -160))
        gen.generate_destructible(pygame.math.Vector2(4192, -160))
        gen.generate_destructible(pygame.math.Vector2(4128, -288), 2)
        gen.generate_destructible(pygame.math.Vector2(5376, -288), 2)
        gen.generate_destructible(pygame.math.Vector2(5472, -288))

        # Create the pipes.
        gen.generate_pipe_body(pygame.math.Vector2(896, -384))
        gen.generate_pipe_top(pygame.math.Vector2(896, -352))
        gen.generate_pipe_body(pygame.math.Vector2(1216, -384), 2)
        gen.generate_pipe_top(pygame.math.Vector2(1216, -320))
        gen.generate_pipe_body(pygame.math.Vector2(1472, -384), 3)
        gen.generate_pipe_top(pygame.math.Vector2(1472, -288))
        gen.generate_pipe_body(pygame.math.Vector2(1824, -384), 3)
        gen.generate_pipe_top(pygame.math.Vector2(1824, -288))
        gen.generate_pipe_body(pygame.math.Vector2(5216, -384))
        gen.generate_pipe_top(pygame.math.Vector2(5216, -352))
        gen.generate_pipe_body(pygame.math.Vector2(5728, -384))
        gen.generate_pipe_top(pygame.math.Vector2(5728, -352))

        # Create the blocks.
        gen.generate_blocks(pygame.math.Vector2(4288, -384), 4)
        gen.generate_blocks(pygame.math.Vector2(4320, -352), 3)
        gen.generate_blocks(pygame.math.Vector2(4352, -320), 2)
        gen.generate_blocks(pygame.math.Vector2(4384, -288))
        gen.generate_blocks(pygame.math.Vector2(4480, -288))
        gen.generate_blocks(pygame.math.Vector2(4480, -320), 2)
        gen.generate_blocks(pygame.math.Vector2(4480, -352), 3)
        gen.generate_blocks(pygame.math.Vector2(4480, -384), 4)
        gen.generate_blocks(pygame.math.Vector2(4736, -384), 5)
        gen.generate_blocks(pygame.math.Vector2(4768, -352), 4)
        gen.generate_blocks(pygame.math.Vector2(4800, -320), 3)
        gen.generate_blocks(pygame.math.Vector2(4832, -288), 2)
        gen.generate_blocks(pygame.math.Vector2(4960, -288))
        gen.generate_blocks(pygame.math.Vector2(4960, -320), 2)
        gen.generate_blocks(pygame.math.Vector2(4960, -352), 3)
        gen.generate_blocks(pygame.math.Vector2(4960, -384), 4)
        gen.generate_blocks(pygame.math.Vector2(5792, -384), 9)
        gen.generate_blocks(pygame.math.Vector2(5824, -352), 8)
        gen.generate_blocks(pygame.math.Vector2(5856, -320), 7)
        gen.generate_blocks(pygame.math.Vector2(5888, -288), 6)
        gen.generate_blocks(pygame.math.Vector2(5920, -256), 5)
        gen.generate_blocks(pygame.math.Vector2(5952, -224), 4)
        gen.generate_blocks(pygame.math.Vector2(5984, -192), 3)
        gen.generate_blocks(pygame.math.Vector2(6016, -160), 2)
        gen.generate_blocks(pygame.math.Vector2(6048, -128))
        gen.generate_blocks(pygame.math.Vector2(6336, -384))

        # Create the hills.
        gen.generate_hill(pygame.math.Vector2(0, -384))
        gen.generate_hill(pygame.math.Vector2(512, -384))
        gen.generate_hill(pygame.math.Vector2(1536, -384))
        gen.generate_hill(pygame.math.Vector2(2048, -384))
        gen.generate_hill(pygame.math.Vector2(3136, -384))
        gen.generate_hill(pygame.math.Vector2(3552, -384))
        gen.generate_hill(pygame.math.Vector2(4672, -384))
        gen.generate_hill(pygame.math.Vector2(5152, -384))
        gen.generate_hill(pygame.math.Vector2(6176, -384))

        # Create the bushes.
        gen.generate_bush(pygame.math.Vector2(384, -384), 4)
        gen.generate_bush(pygame.math.Vector2(736, -384))
        gen.generate_bush(pygame.math.Vector2(1312, -384), 3)
        gen.generate_bush(pygame.math.Vector2(1920, -384), 4)
        gen.generate_bush(pygame.math.Vector2(2304, -384))
        gen.generate_bush(pygame.math.Vector2(2880, -384), 3)
        gen.generate_bush(pygame.math.Vector2(3424, -384), 4)
        gen.generate_bush(pygame.math.Vector2(3840, -384))
        gen.generate_bush(pygame.math.Vector2(4416, -384))
        gen.generate_bush(pygame.math.Vector2(5376, -384))

        # Create the clouds.
        gen.generate_cloud(pygame.math.Vector2(288, -128))
        gen.generate_cloud(pygame.math.Vector2(608, -96))
        gen.generate_cloud(pygame.math.Vector2(896, -128), 4)
        gen.generate_cloud(pygame.math.Vector2(1184, -96), 3)
        gen.generate_cloud(pygame.math.Vector2(1792, -128))
        gen.generate_cloud(pygame.math.Vector2(2176, -96))
        gen.generate_cloud(pygame.math.Vector2(2400, -128), 4)
        gen.generate_cloud(pygame.math.Vector2(2720, -96), 3)
        gen.generate_cloud(pygame.math.Vector2(3328, -128))
        gen.generate_cloud(pygame.math.Vector2(3680, -96))
        gen.generate_cloud(pygame.math.Vector2(3968, -128), 4)
        gen.generate_cloud(pygame.math.Vector2(4256, -96), 3)
        gen.generate_cloud(pygame.math.Vector2(4896, -128))
        gen.generate_cloud(pygame.math.Vector2(5248, -96))
        gen.generate_cloud(pygame.math.Vector2(5504, -128), 4)
        gen.generate_cloud(pygame.math.Vector2(5792, -96), 3)
        gen.generate_cloud(pygame.math.Vector2(6432, -128))

        # Return the level data generated for this section.
        return data
    
    # Is this the "other" section?
    elif section == "other":
        # Create the level generator and level data for this section.
        gen = levelgenerator.LevelGenerator(engine, level, "underground")
        data = Level11_main(engine, level, pygame.math.Vector2(0, 0), "underground")

        # Temp.
        gen.generate_ground(pygame.math.Vector2(0, -416), 50, 2)
        
        # Return the level data generated for this section.
        return data