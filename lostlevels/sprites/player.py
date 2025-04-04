"""This is the Lost Levels player sprite, which can be controlled
by the player."""

import pygame
import engine
import time

# The player class.
class Player(engine.entity.Sprite):
    # Construct a new player.
    def __init__(self, engine, classname):
        # Call the entity constructor and modify its default properties.
        super().__init__(engine, classname)
        self.get_event("per_frame").set_func(Player.per_frame)
        self.get_event("collision").set_func(Player.collision)
        self.get_event("collisionfinal").set_func(Player.collisionfinal)
        self.acceleration = 6.5

        # Load the player spritesheet.
        self.load("lostlevels/assets/sprites/player_small.png", (24, 58), 10)

        # Cache the status of the player jumping.
        self.__jumping = 0
        self.__speedwhenjumping = 0

        # Store the timestamp for when the player's animation last changed.
        self.__animtimestamp = 0

        # Cache the status of the player crouching.
        self.__crouching = False

        # Can this player actually move?
        self.moveable = True

        # Main player status.
        self.alive = True

        # The level scene object.
        self.level = None

    # Handle player movement per-frame.
    def per_frame(self):
        # Return if this player can't move.
        if not self.moveable:
            return

        # Accelerate the player in either direction based on which arrow
        # keys are held.
        keys = self._engine.get_keys_dict()
        self.move = 0
        if keys[pygame.K_LEFT]:
            self.move -= 150
        if keys[pygame.K_RIGHT]:
            self.move += 150

        # Accelerate faster if the Z key is held.
        if keys[pygame.K_z]:
            self.move *= 1.75

        # Jump upon pressing X.
        if keys[pygame.K_x]:
            # Set the timestamp where the player kept jumping.
            if self.groundentity and self.__jumping == -1:
                self.__jumping = time.perf_counter()
                self.__speedwhenjumping = abs(self.velocity.x)
            
            # Hold the player upwards depending on whether they are holding the X key
            # and how fast they're moving.
            multiplier = max(min(abs(self.__speedwhenjumping), 150) / 125, 1)
            if self.__jumping + 0.3 > time.perf_counter():
                self.velocity.y = 350 * multiplier
        else:
            self.__jumping = -1

        # Handle crouching upon pressing the downwards arrow key and set the
        # player's hitbox size.
        if self.groundentity:
            # Set the crouching state.
            if keys[pygame.K_DOWN]:
                if not self.__crouching:
                    self.__crouching = True
                    self.set_hitbox(pygame.math.Vector2(24, 30))
                    self.set_baseorigin(self.get_baseorigin() - pygame.math.Vector2(0, 28))
            else:
                if self.__crouching:
                    self.set_hitbox(pygame.math.Vector2(24, 58))
                    self.set_baseorigin(self.get_baseorigin() + pygame.math.Vector2(0, 28))
                self.__crouching = False

            # Nullify any ground movment while crouching.
            if self.__crouching:
                self.move = 0

        # Flip the player sprite in the direction of travel.
        if abs(self.velocity.x) > 0.1:
            self.flip(self.velocity.x < 0)
        
        # Animate the player based on its current movement.
        if self.__crouching:
            self.index = 5
        else:
            if self.groundentity:
                if abs(self.velocity.x) > 0.1:
                    length = 1 / (abs(self.velocity.x) / 20)
                    if time.perf_counter() > self.__animtimestamp + length:
                        self.__animtimestamp = time.perf_counter()
                        self.index = (self.index % 3) + 1
                else:
                    self.index = 0
            else:
                self.index = 4

    # Override the player's collision.
    def collision(self, other, coltype, coldir):
        # If this player is alive, handle collision in all cases.
        if self.alive:
            return True
        
        # Otherwise, do not collide with anything.
        return False

    # Handle additional collision resolution code.
    def collisionfinal(self, other, coltype, coldir):
        # If this player hit another entity from below, stop jumping.
        if ((coltype == engine.entity.COLTYPE_COLLIDING and coldir == engine.entity.COLDIR_DOWN)
            or (coltype == engine.entity.COLTYPE_COLLIDED and coldir == engine.entity.COLDIR_UP)):
            self.__jumping = -1
        
        # If this player was hit by a falling entity, kill the player.
        if (coltype == engine.entity.COLTYPE_COLLIDED and coldir == engine.entity.COLDIR_UP
            and self.level):
            self.level.death()

    # Use an entity by utilizing the USE key.
    def keydown(self, enum, unicode, focused):
        # Check that this is the USE key.
        if not enum == pygame.K_e:
            return

        # Generate a list of entities close to the player.
        start = self.get_topleft() + pygame.math.Vector2(-30, 30)
        end = self.get_bottomright() + pygame.math.Vector2(30, -30)
        entities = self._engine.query_entities(start, end)

        # Find the closest entity to the player that can be used.
        closest = None
        closest_dist = 0
        for entity in entities:
            if not entity.can_use:
                continue
            diff = entity.get_centre() - self.get_centre()
            dist = diff.x ** 2 + diff.y ** 2
            if not closest or dist < closest_dist:
                closest = entity

        # Invoke the use event of the selected entity, if found.
        if closest:
            closest.invoke_event("use")

    # Kill this player.
    def kill(self):
        # Invalidate the player's alive status.
        self.alive = False

        # Change the player to the death pose.
        self.moveable = False
        self.index = 7
        self.velocity = pygame.math.Vector2(0, 500)
        self.move = 0

        # Log the player's death.
        self._engine.console.log("[Lost Levels]: the player has died!")