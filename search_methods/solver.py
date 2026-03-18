from sokoban.map import Map
from search_methods.beam_search import beam_search
from search_methods.ida_star import ida
from search_methods.heuristics import minimum_matching
import time


class Solver:

    def __init__(self, map: Map) -> None:
        self.map = map

    def solve(self):
        raise NotImplementedError

    def solve_beam(map: Map):
        start = time.time()

        solved, explored = beam_search(map, 5, minimum_matching)

        duration = time.time() - start

        if solved is True:
            return duration, explored
        else:
            return None
        
    def solve_ida_star(map: Map):
        start = time.time()

        solved, explored = ida(map, minimum_matching)

        duration = time.time() - start

        if solved is True:
            return duration, explored
        else:
            return None