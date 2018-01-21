#!/usr/bin/env python
"""
This is a bot that applies propositional logic reasoning to determine its strategy.
The strategy it uses is determined by what is defined in load.py. Here it is to always
pick a Jack to play whenever this is a legal move.

It loads general information about the game, as well as the definition of a strategy,
from load.py.
"""

from api import State
import random, load2

from bots.kbbot.kb import KB, Boolean


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        moves = state.moves()
        random.shuffle(moves)

        player = state.whose_turn()
        onlead = state.leader()

        if player == onlead:
            # Check for possible Trump Exchange
            for move in moves:
                if not self.kb_consistent_trump_exchange(state, move):
                    print "Trump exchange strategy Applied"
                    return move

            # Check for possible weddings
            for move in moves:

                if not self.kb_consistent_marriage(state, move):
                    print "Wedding strategy Applied"
                    return move

            for move in moves:

                if not self.kb_consistent_low_non_trump(state, move):
                    print "Low non trump strategy Applied"
                    return move
        else:
            print "random move made"
            return random.choice(moves)



        # If no move that is entailed by the kb is found, play random move
        return random.choice(moves)

    # Note: In this example, the state object is not used,
    # but you might want to do it for your own strategy.
    def kb_consistent_marriage(self, state, move):
        # type: (State, move) -> bool

        kb = KB()
        load2.general_information(kb)
        load2.strategy_knowledge(kb)

        card1 = move[0]
        card2 = move[1]

        if card2 is not None:
            if card1 > card2:
                variable_string = "m" + str(card1) + str(card2)
            else:
                variable_string = "m" + str(card2) + str(card1)

            strategy_variable = Boolean(variable_string)
            kb.add_clause(~strategy_variable)
            return kb.satisfiable()

        return True

    def kb_consistent_trump_exchange(self, state, move):
        # type: (State, move) -> bool

        kb = KB()
        load2.general_information(kb)
        load2.strategy_knowledge(kb)

        index = move[1]

        if index is not None:
            variable_string = "te" + str(index)
            strategy_variable = Boolean(variable_string)

            kb.add_clause(~strategy_variable)

            return kb.satisfiable()

        return True

    def kb_consistent_low_non_trump(self, state, move):
        # type: (State, move) -> bool

        kb = KB()

        load2.general_information(kb)
        load2.strategy_knowledge(kb)

        card = move[0]
        trump_suit = state.get_trump_suit()
        print "card: {}, suit:, {}".format(card, trump_suit)

        variable_string = "pc" + str(card)
        strategy_variable = Boolean(variable_string)
        trump_suit_string = "T" + str(trump_suit)
        trump_variable = Boolean(trump_suit_string)

        kb.add_clause(~strategy_variable)
        kb.add_clause(~trump_variable)

        return kb.satisfiable()


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
