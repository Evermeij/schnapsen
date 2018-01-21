#!/usr/bin/env python
"""
This is a bot that applies propositional logic reasoning to determine its strategy.
The strategy it uses is determined by what is defined in load.py. Here it is to always
pick a Jack to play whenever this is a legal move.

It loads general information about the game, as well as the definition of a strategy,
from load.py.
"""

from api import State, util
import random, load2

from kb import KB, Boolean, Integer


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()

        random.shuffle(moves)

        for move in moves:

            if not self.kb_consistentTM(state, move):
                # Plays the first move that makes the kb inconsistent. We do not take
                # into account that there might be other valid moves according to the strategy.
                # Uncomment the next line if you want to see that something happens.
                print "Strategy Applied"
                return move

        # If no move that is entailed by the kb is found, play random move
        return random.choice(moves)

    # Note: In this example, the state object is not used,
    # but you might want to do it for your own strategy.
    def kb_consistentTM(self, state, move):
        # type: (State, move) -> bool

        kb = KB()

        load2.general_information(kb)

        load2.strategy_knowledge(kb)

        card1 = move[0]
        card2 = move[1]

        if card2 is not None:
            variable_string = "tm" + str(card1) + str(card2)
            strategy_variable = Boolean(variable_string)

            kb.add_clause(~strategy_variable)

            return kb.satisfiable()

        return True
        
    def kb_consistent(self, state, move):
        # type: (State, move) -> bool

        kb = KB()

        load2.general_information(kb)

        load2.strategy_knowledge(kb)

        index = move[0]

        variable_string = "pc" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()