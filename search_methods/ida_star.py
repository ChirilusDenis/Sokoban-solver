from sokoban import *
from search_methods import heuristics

def ida(start : Map, h) :
    heuristics.table = {}
    limit = h(start)
    global explored
    global undo
    undo = 0
    explored = 0
    path = [start]

    while True:
        vis = {str(start)}
        r = DF(path, 0, limit, h, vis)
        if r is True: return True, explored, undo
        if r is False: return False
        limit = r


def DF(path: list[Map], g, limit, h, vis):
    global explored
    global undo
    state = path[-1]
    
    temp = h(state)
    if temp is False: return False

    if g + temp > limit: return g + temp
    if state.is_solved():
        undo = state.undo_moves
        return True
    min = False
    for neigh in state.get_neighbours():
        if str(neigh) not in vis:
            path.append(neigh)
            vis.add(str(neigh))
            explored += 1
            r = DF(path, g + 1, limit, h, vis)
            if r is True: return True
            if r is not False and (min is False or r < min): min = r
            path.pop()
    return min