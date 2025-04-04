"""This is the entry-level module for the entire program's structure.

This will immediately instantiate the engine, pointing to the per-frame function
defined in the lostlevels package."""

import engine
import engine.logger
import lostlevels
 
# Instantiate and run the engine.
eng = engine.LLEngine("Lost Levels")
game = lostlevels.LostLevels(eng)
eng.set_game(game)
eng.init()