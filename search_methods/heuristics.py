import itertools
from sokoban import Map
from sokoban.map import OBSTACLE_SYMBOL
# 1
# first implemented heuristic, it gets stuck on the simplest test because it doesnt
# account for obstacles in the pursuit to bring the box closer
# _ _ X
# _ / /
# _ _ B

def manhatan_total(state : Map, good):
    p = (state.player.x, state.player.x) # (x,  y) of player
    b = [(b.x, b.y) for b in state.boxes.values()] # [(x, y)] of all boxes
    t = state.targets # [(x, y)] of all targets

    target_imp = 10 # how much more important it is to bring a box closer to a target
                    # compared to moving closer to a box

    p_b = 0
    for coords in b: # manhatan distance between player and all boxes
        if coords not in good: return False
        p_b += abs(coords[0] - p[0]) + abs(coords[1] - p[1])

    t_b = 0
    for pos_b in b: # manhatan distance between all targets and all boxes
        for pos_t in t:
            t_b += abs(pos_b[0] - pos_t[0]) + abs(pos_b[1] - pos_t[1])

    return p_b + target_imp * t_b

# 2
# solves first map
# on second test, this algorith does a pull move and gets stuck
# _ X       _ P
# / _ ====> / B
# _ P       _ _
# _ B       _ _

calc = {}
good = set()

def aprox_box_dist(state : Map):
    p = (state.player.x, state.player.x) # (x,  y) of player
    b = [(b.x, b.y) for b in state.boxes.values()] # [(x, y)] of all boxes
    t = state.targets # [(x, y)] of all targets

    global good
    global calc

    if len(good) == 0:
        print("made good")
        good = non_deadlock(state)


    box_dist = 0 # pushes needed for all boxes to get to target with walls
    for box in b:
        if box not in good: return False

        # used to store previous calculations
        if calc.get(box) == None:
            d = pushes_box_closest_target(state, box, t)

        else: d = calc[box]#[0]

        if d is False: return False
        box_dist += d

    player_boxes = 0 # manhatan distance between player and all boxes

    if len(b) != 0:
        player_boxes = min(map(lambda coords : abs(coords[0] - p[0]) + abs(coords[1] - p[1]), b))

    # importance of bringing box->target / player->box
    target_imp = 2 # lower numbers make easy 1 go slower
    return player_boxes + target_imp * box_dist

# count the minimum number of pushes it would take for the box to get to the target
# in the simplest way, accounting for walls
def pushes_box_closest_target(map : Map, start : tuple[int, int], target : list[tuple[int, int]]):
    global calc
    q = [(start, 0)]
    vis = set()
    while len(q) != 0:
        crt = q.pop()
        pos = crt[0]
        if crt[0] in target:
            calc[pos] = crt[1]
            return crt[1]

        if pos[0] >= 1 and map.map[pos[0] - 1][pos[1]] != OBSTACLE_SYMBOL:
            if (pos[0] - 1, pos[1]) not in vis:
                vis.add((pos[0] - 1, pos[1]))
                q.insert(0, ((pos[0] - 1, pos[1]), crt[1] + 1))

        if pos[0] < map.length - 1 and map.map[pos[0] + 1][pos[1]] != OBSTACLE_SYMBOL:
            if (pos[0] + 1, pos[1]) not in vis:
                vis.add((pos[0] + 1, pos[1]))
                q.insert(0, ((pos[0] + 1, pos[1]), crt[1] + 1))

        if pos[1] >= 1 and map.map[pos[0]][pos[1] - 1] != OBSTACLE_SYMBOL:
            if (pos[0], pos[1] - 1) not in vis:
                vis.add((pos[0], pos[1] - 1))
                q.insert(0, ((pos[0], pos[1] - 1), crt[1] + 1))

        if pos[1] < map.width - 1 and map.map[pos[0]][pos[1] + 1] != OBSTACLE_SYMBOL:
            if (pos[0], pos[1] + 1) not in vis:
                vis.add((pos[0], pos[1] + 1))
                q.insert(0, ((pos[0], pos[1] + 1), crt[1] + 1))

    return False

# 3 return box coords that arent simple deadlocks
# made old alg check is any box in deadlock spot
# in medium 2 it gets stuck trying to fit 2 boxes in one target

# 3.1 reuse distance calc from pervoious runs
# 3.2 removed solved boxes and targets (idk if it makes things better)

def non_deadlock(map : Map): # e ok pentru tot pana la medium 2
    vis = set()
    for start in map.targets:
        q = [start]
        vis.add(start)
        while len(q) != 0:
            pos = q.pop()

            if pos[0] >= 2 and map.map[pos[0] - 1][pos[1]] != OBSTACLE_SYMBOL and map.map[pos[0] - 2][pos[1]] != OBSTACLE_SYMBOL:
                if (pos[0] - 1, pos[1]) not in vis:
                    vis.add((pos[0] - 1, pos[1]))
                    q.insert(0, (pos[0] - 1, pos[1]))

            if pos[0] < map.length - 2 and map.map[pos[0] + 1][pos[1]] != OBSTACLE_SYMBOL and map.map[pos[0] + 2][pos[1]] != OBSTACLE_SYMBOL:
                if (pos[0] + 1, pos[1]) not in vis:
                    vis.add((pos[0] + 1, pos[1]))
                    q.insert(0, (pos[0] + 1, pos[1]))

            if pos[1] >= 2 and map.map[pos[0]][pos[1] - 1] != OBSTACLE_SYMBOL and map.map[pos[0]][pos[1] - 2] != OBSTACLE_SYMBOL:
                if (pos[0], pos[1] - 1) not in vis:
                    vis.add((pos[0], pos[1] - 1))
                    q.insert(0, (pos[0], pos[1] - 1))

            if pos[1] < map.width - 2 and map.map[pos[0]][pos[1] + 1] != OBSTACLE_SYMBOL and map.map[pos[0]][pos[1] + 2] != OBSTACLE_SYMBOL:
                if (pos[0], pos[1] + 1) not in vis:
                    vis.add((pos[0], pos[1] + 1))
                    q.insert(0, (pos[0], pos[1] + 1))
    return vis


# 4
# maybe assign each box a target
# use minimum matching
# YES it solves medium 2 too

table = {}
def min_match(state: Map):
    b = [(box.x, box.y) for box in state.boxes.values()]
    t = state.targets
    global table

    for start in state.targets:
        vis = set()
        q = [(start, 0)]
        vis.add(start)
        while len(q) != 0:
            crt = q.pop()
            pos = crt[0]

            if pos in b:
                table[(pos, start)] = crt[1]

            if pos[0] >= 2 and state.map[pos[0] - 1][pos[1]] != OBSTACLE_SYMBOL and state.map[pos[0] - 2][pos[1]] != OBSTACLE_SYMBOL:
                if (pos[0] - 1, pos[1]) not in vis:
                    vis.add((pos[0] - 1, pos[1]))
                    q.insert(0, ((pos[0] - 1, pos[1]), crt[1] + 1))

            if pos[0] < state.length - 2 and state.map[pos[0] + 1][pos[1]] != OBSTACLE_SYMBOL and state.map[pos[0] + 2][pos[1]] != OBSTACLE_SYMBOL:
                if (pos[0] + 1, pos[1]) not in vis:
                    vis.add((pos[0] + 1, pos[1]))
                    q.insert(0, ((pos[0] + 1, pos[1]), crt[1] + 1))

            if pos[1] >= 2 and state.map[pos[0]][pos[1] - 1] != OBSTACLE_SYMBOL and state.map[pos[0]][pos[1] - 2] != OBSTACLE_SYMBOL:
                if (pos[0], pos[1] - 1) not in vis:
                    vis.add((pos[0], pos[1] - 1))
                    q.insert(0, ((pos[0], pos[1] - 1), crt[1] + 1))

            if pos[1] < state.width - 2 and state.map[pos[0]][pos[1] + 1] != OBSTACLE_SYMBOL and state.map[pos[0]][pos[1] + 2] != OBSTACLE_SYMBOL:
                if (pos[0], pos[1] + 1) not in vis:
                    vis.add((pos[0], pos[1] + 1))
                    q.insert(0, ((pos[0], pos[1] + 1), crt[1] + 1))

        for box in b:
            if table.get((box, start)) is None:
                table[(box, start)] = 1000
        
    combos = [list(zip(x,t)) for x in itertools.permutations(b,len(t))]
    m = None
    for perm in combos:
        s = sum(table[x] for x in perm)
        if m is None or s < m: m = s

    p = (state.player.x, state.player.y)
    player_boxes = min(map(lambda coords : abs(coords[0] - p[0]) + abs(coords[1] - p[1]), b))
    target_imp = 2
    return player_boxes + target_imp * m

# 4.1
# made it so the search is done from boxes to targets


# 4.2
# added min player box distance made it much faster
# from 1:34 -> 0:15 for medium 2

# 4.3
# optimised, dont recalculate is I have a dist
# now it solves all easy and medium maps
# 0:15 -> 0:05 for medium 2
# on hard 1 gets stuck next to 2 boxes because

# 4.4
# made min player box distance to min distance to unsolved boxes
# 0:05 -> 0:01.7
# it also makes hard 1 get stuck earlier
# \ _ P _ 
# _ \ B _
# _ _ B _
# <- more boxes that way

# UNDONE
# 4.5 made the player box distance the sum of distances to unsolved targets
# 0:01.7 -> 0:00.1 for medium 2
# now it solves everything until and including hard 1

def dist_box_all_targets(map: Map, box):
    global table
    q = [(box, 0)]
    vis = set()
    vis.add(box)
    while len(q) != 0:
        crt = q.pop()
        pos = crt[0]
        d = crt[1]

        if pos in map.targets:
            table[(box, pos)] = d

        if pos[0] > 0 and map.map[pos[0] - 1][pos[1]] != OBSTACLE_SYMBOL:
            if pos[0] < map.length - 1 and map.map[pos[0] + 1][pos[1]] != OBSTACLE_SYMBOL:
                if (pos[0] - 1, pos[1]) not in vis:
                    vis.add((pos[0] - 1, pos[1]))
                    q.insert(0, ((pos[0] - 1, pos[1]), d + 1))
                if (pos[0] + 1, pos[1]) not in vis:
                    vis.add((pos[0] + 1, pos[1]))
                    q.insert(0, ((pos[0] + 1, pos[1]), d + 1))

        if pos[1] >= 1 and map.map[pos[0]][pos[1] - 1] != OBSTACLE_SYMBOL:
            if pos[1] < map.width - 1 and map.map[pos[0]][pos[1] + 1] != OBSTACLE_SYMBOL:
                if (pos[0], pos[1] - 1) not in vis:
                    vis.add((pos[0], pos[1] - 1))
                    q.insert(0, ((pos[0], pos[1] - 1), d + 1))
                if (pos[0], pos[1] + 1) not in vis:
                    vis.add((pos[0], pos[1] + 1))
                    q.insert(0, ((pos[0], pos[1] + 1), d + 1))


    # cant reach target t from box position
    for t in map.targets:
        if table.get((box, t)) is None:
            table[(box, t)] = 1000

def minimum_matching(state: Map):
    b = [(box.x, box.y) for box in state.boxes.values()]
    t = state.targets

    unsolved = [box for box in b if box not in set(t)]

    global table
    for box in b:
        if table.get((box, t[0])) is None:
            dist_box_all_targets(state, box)

    combos = [list(zip(x,t)) for x in itertools.permutations(b,len(t))]
    m = None
    for perm in combos:
        s = sum(table[x] for x in perm)
        if m is None or s < m:
            m = s

    p = (state.player.x, state.player.y)
    player_boxes = 0
    if len(unsolved) != 0:
        player_boxes = min(map(lambda coords: abs(coords[0] - p[0]) + abs(coords[1] - p[1]), unsolved))
    target_imp = 5
    return player_boxes + target_imp * m

 