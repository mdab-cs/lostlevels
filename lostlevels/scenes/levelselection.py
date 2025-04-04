"""The level selection scene for Lost Levels."""

import pygame
import engine

from .. import levelinfo

# World portal.
class WorldPortal(engine.entity.Tile):
    # Construct the world portal entity.
    def __init__(self, engine, classname):
        # Call the tile constructor and add new properties.
        super().__init__(engine, classname)
        self.world = 0

# Level selection scene.
class LevelSelection(engine.Game):
    # Construct the level selection map.
    def __init__(self, eng, game):
        # Initialize the game interface.
        super().__init__(eng)
        self.__game = game
        self._engine.console.log("[Lost Levels]: launching level selection map")

        # Register WorldPortal as an engine entity type.
        self._engine.register_classname("worldportal", WorldPortal)

        # Create the background.
        self.room = self._engine.create_ui_element_by_class("image", engine.ui.LAYER_BACKGROUND)
        self.room.load("lostlevels/assets/biomes/levelselection/background.png")
        self.room.set_size(engine.ui.UDim2(1, 0, 1, 0))
        self.room.enabled = True

        # Load the level selection map music.
        self.music = self._engine.create_sound(
            "lostlevels/assets/audio/levelselection/sma4_world_e_castle.ogg")
        self.music.volume = 1
        self.music.play(True)

        # Create an invisible rectangle for the ground.
        self.ground = self._engine.create_entity_by_class("rect")
        self.ground.set_hitbox(pygame.math.Vector2(576, 65))
        self.ground.set_baseorigin(pygame.math.Vector2(0, -415))
        self.ground.draw = False
        self._engine.activate_entity(self.ground)

        # Create an invisible wall on the left-hand side of the map.
        self.leftwall = self._engine.create_entity_by_class("rect")
        self.leftwall.set_hitbox(pygame.math.Vector2(10, 480))
        self.leftwall.set_baseorigin(pygame.math.Vector2(-10, 0))
        self.leftwall.draw = False
        self._engine.activate_entity(self.leftwall)

        # Create an invisible wall on the right-hand side of the map.
        self.rightwall = self._engine.create_entity_by_class("rect")
        self.rightwall.set_hitbox(pygame.math.Vector2(10, 480))
        self.rightwall.set_baseorigin(pygame.math.Vector2(576, 0))
        self.rightwall.draw = False
        self._engine.activate_entity(self.rightwall)

        # Create the world portals.
        for i in range(0, levelinfo.NUM_WORLDS):
            portal = self._engine.create_entity_by_class("worldportal")
            portal.movetype = engine.entity.MOVETYPE_NONE
            portal.load("lostlevels/assets/temp.png", (128, 128), i)
            portal.set_hitbox(pygame.math.Vector2(128, 200))
            portal.set_baseorigin(pygame.math.Vector2(32 + i * 192, -159))
            portal.world = i + 1
            portal.can_use = True
            portal.get_event("use").set_func(lambda elem: self.load_world(elem))
            self._engine.activate_entity(portal)
        
        # Create the player sprite.
        self.player = self._engine.create_entity_by_class("player")
        self.player.set_baseorigin(pygame.math.Vector2(50, -200))
        self._engine.activate_entity(self.player)

    # Handle exiting back to the main menu and forward keydown events
    # to the player.
    def keydown(self, enum, unicode, focused):
        # Return to the main menu if the ESC key is pressed.
        if enum == pygame.K_ESCAPE:
            self.music.stop()
            self.__game.load_startmenu()

        # Forward this event to the player.
        self.player.keydown(enum, unicode, focused)

    # Load a new world.
    def load_world(self, portal, started = False):
        # Return if the player is grounded.
        if not started and not self.player.groundentity:
            return

        # If the player just selected the USE key, show a jump "animation"
        # and call this method again half-a-second later to initiate the
        # world-loading sequence.
        if not started:
            self._engine.console.log(f"[Lost Levels]: loading world {portal.world}")
            self.player.moveable = False
            self.player.index = 4
            self.player.velocity.y = 650
            self.player.velocity.x = 0
            self.player.move = 0
            self._engine.create_timer(self.load_world, 0.5, portal, True)
        else:
            self.music.stop()
            self.__game.load_world(portal.world)