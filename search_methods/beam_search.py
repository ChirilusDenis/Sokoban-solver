from sokoban import *
import numpy as np
import builtins
from search_methods import heuristics

def softmax(x: np.array) -> float:
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def beam_search(start : Map, B : int, h):
    np.random.seed(0)
    heuristics.table = {}
    limit = 1000000
    explored = 0
    beam = [start]
    vis = {str(start)}

    while len(beam) != 0 and len(vis) < limit:
        succ = []
        for state in beam:
            for neigh in state.get_neighbours():
                # if neigh not in vis:
                if str(neigh) not in vis:
                    if neigh.is_solved():
                        return True, explored, neigh.undo_moves
                    succ.append(neigh)
                    explored += 1

        top = sorted(succ, key=h)[0:B]
        beam = top
        vis |= {str(b) for b in beam}

    return False, explored

        