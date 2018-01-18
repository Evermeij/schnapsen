"""
RandomBot -- A simple strategy: enumerates all legal moves, and picks one
uniformly at random.
"""

# Import the API objects
from api import State, util
import random


def heuristics(state, player):
    return util.ratio_points(state, player)


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        """
        Function that gets called every turn. This is where to implement the strategies.
        Be sure to make a legal move. Illegal moves, like giving an index of a card you
        don't own or proposing an illegal mariage, will lose you the game.
       	TODO: add some more explanation
        :param State state: An object representing the gamestate. This includes a link to
            the states of all the cards, the trick and the points.
        :return: A tuple of integers or a tuple of an integer and None,
            indicating a move; the first indicates the card played in the trick, the second a
            potential spouse.
        """

        player = state.whose_turn()

        # All legal moves
        moves = state.moves()
        dept = 2
        best_score = float("-inf")
        best_move = random.choice(moves)

        for move in moves:
            score = self.evaluate(state.next(move), player, dept)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def evaluate(self, state, player, dept):
        # type: () -> float

        dept = dept - 1
        st = state.clone()
        score = 1
        new_moves = st.moves()

        for new_move in new_moves:
            if st.finished():
                break
            if dept > 0:
                score += self.evaluate(st.next(new_move), player, dept)
            else:
                st2 = st.clone()
                for i in range(10):
                    if st2.finished():
                        break
                    st2 = st2.next(random.choice(st2.moves()))

                score += heuristics(st2, player)

        if len(new_moves) > 0:
            return score/float(len(new_moves))
        else:
            return score
