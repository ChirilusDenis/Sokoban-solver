
import itertools
from search_methods import beam_search
from search_methods.beam_search import beam_search
from search_methods.heuristics import manhatan_total, min_match, minimum_matching, non_deadlock, pushes_box_closest_target, aprox_box_dist
from search_methods.ida_star import ida
from sokoban import *
# from search_methods import *
import random
import time
from search_methods.solver import Solver
import pandas as pd
import matplotlib.pyplot as plt

from sokoban.map import OBSTACLE_SYMBOL

# map = Map(5, 5, 0, 0, [('box1', 1, 3)], [(4, 4)], [(3,3), (3,4), (3,1)], 'easy_map1')
map1 = Map.from_yaml('tests/easy_map1.yaml')
map2 = Map.from_yaml('tests/easy_map2.yaml')
map3 = Map.from_yaml('tests/medium_map1.yaml')
map4 = Map.from_yaml('tests/medium_map2.yaml')
map5 = Map.from_yaml('tests/hard_map1.yaml')
map6 = Map.from_yaml('tests/hard_map2.yaml')
map7 = Map.from_yaml('tests/large_map1.yaml')
map8 = Map.from_yaml('tests/large_map2.yaml')
map9 = Map.from_yaml('tests/super_hard_map1.yaml')

# print(map)

#tuplu de 0 = vertical ^
#tuplu de 1 = horixontal >
# p = (map.player.x, map.player.x) # (x,  y) of player
# b = [(b.x, b.y) for b in map.boxes.values()] # [(x, y)] of all boxes
# t = map.targets # [(x, y)] of all targets
# # print(b)

# p_b = 0
# for coords in b: # manhatan distance between player and all boxes
#     p_b += abs(coords[0] - p[0]) + abs(coords[1] - p[1])

# print(p_b)

# steps = 0
# limit = 10
# while steps < limit:
#     steps += 1
#     neigh = map.get_neighbours()
#     if len(neigh) == 0: break
#     # print(map)
#     map = random.choice(neigh)

# print(beam_search.beam_search(map, 5, manhatan_total, 100))
# print(ida(map, manhatan_total))

# print(pushes_box_closest_target(map, b[0], t))
# print(ida(map, aprox_box_dist))

# s = map.__str__()

# s = s.replace("P", "_").replace("B", "_").replace("X", "_")
# new_map = Map.from_str(s)

# t = map.targets
# o = map.obstacles
# for tar in t:
#     if tar[0] > 0 and map.map[tar[0] - 1][tar[1]] != OBSTACLE_SYMBOL:
#         new_map = Map(map.length, map.width, tar[0] - 1, tar[1], [("box", tar[0], tar[1])], [], o)

#     if tar[0] < map.length - 1 and map.map[tar[0] + 1][tar[1]] != OBSTACLE_SYMBOL:
#         new_map = Map(map.length, map.width, tar[0] + 1, tar[1], [("box", tar[0], tar[1])], [], o)

#     if tar[1] > 0 and map.map[tar[0]][tar[1] - 1] != OBSTACLE_SYMBOL:
#         new_map = Map(map.length, map.width, tar[0], tar[1] - 1, [("box", tar[0], tar[1])], [], o)

#     if tar[1] < map.width - 1 and map.map[tar[0]][tar[1] + 1] != OBSTACLE_SYMBOL:
#         new_map = Map(map.length, map.width, tar[0], tar[1] + 1, [("box", tar[0], tar[1])], [], o)
# new_map = Map(map.length, map.width, 0, 0, [], [], o)
# def idk(map: Map):
    # vis = set()
    # for start in map.targets:
    #     q = [start]
    #     vis.add(start)
    #     while len(q) != 0:
    #         pos = q.pop()

    #         if pos[0] >= 2 and map.map[pos[0] - 1][pos[1]] != OBSTACLE_SYMBOL and map.map[pos[0] - 2][pos[1]] != OBSTACLE_SYMBOL:
    #             if (pos[0] - 1, pos[1]) not in vis:
    #                 vis.add((pos[0] - 1, pos[1]))
    #                 q.insert(0, (pos[0] - 1, pos[1]))

    #         if pos[0] < map.length - 2 and map.map[pos[0] + 1][pos[1]] != OBSTACLE_SYMBOL and map.map[pos[0] + 2][pos[1]] != OBSTACLE_SYMBOL:
    #             if (pos[0] + 1, pos[1]) not in vis:
    #                 vis.add((pos[0] + 1, pos[1]))
    #                 q.insert(0, (pos[0] + 1, pos[1]))

    #         if pos[1] >= 2 and map.map[pos[0]][pos[1] - 1] != OBSTACLE_SYMBOL and map.map[pos[0]][pos[1] - 2] != OBSTACLE_SYMBOL:
    #             if (pos[0], pos[1] - 1) not in vis:
    #                 vis.add((pos[0], pos[1] - 1))
    #                 q.insert(0, (pos[0], pos[1] - 1))

    #         if pos[1] < map.width - 2 and map.map[pos[0]][pos[1] + 1] != OBSTACLE_SYMBOL and map.map[pos[0]][pos[1] + 2] != OBSTACLE_SYMBOL:
    #             if (pos[0], pos[1] + 1) not in vis:
    #                 vis.add((pos[0], pos[1] + 1))
    #                 q.insert(0, (pos[0], pos[1] + 1))
    # return vis

# print(map)
# print(non_deadlock(map))

# print(ida(map, aprox_box_dist))
# print(map1)
# print(min_match(map4))
# print(ida(map4, min_match))
# print(map5)
# map5.plot_map()
# map6.plot_map()
# print(ida(map9, minimum_matching))

# start_time = time.time()
# print(beam_search(map9, 10, minimum_matching))
# print(ida(map1, minimum_matching))
# print("--- %s seconds ---" % (time.time() - start_time))

# map = map1
# start_time = time.time()

# print(ida(map, minimum_matching))

# checkpoint = time.time()

# print(beam_search(map2, 5, minimum_matching))
# print(Solver.solve_beam(map1))
# print(Solver.solve_beam(map2))
# print(Solver.solve_beam(map3))
# print(Solver.solve_beam(map4))
# print(Solver.solve_beam(map5))
# print(Solver.solve_beam(map6))
# print(Solver.solve_beam(map7))
# print(Solver.solve_beam(map8))
# print(Solver.solve_beam(map9))

# print(beam_search(map1, 5, minimum_matching))
# print(beam_search(map2, 5, minimum_matching))
# print(beam_search(map3, 5, minimum_matching))
# print(beam_search(map4, 5, minimum_matching))
# print(beam_search(map5, 5, minimum_matching))
# print(beam_search(map6, 5, minimum_matching))
# print(beam_search(map7, 5, minimum_matching))
# print(beam_search(map8, 5, minimum_matching))
# print(beam_search(map9, 5, minimum_matching))


# print("IDA  --- %s seconds\n" % (checkpoint - start_time))
# print("Beam --- %s seconds" % (time.time() - checkpoint))

maps = []
maps.append((Map.from_yaml('tests/easy_map1.yaml'), "easy 1"))
maps.append((Map.from_yaml('tests/easy_map2.yaml'), "easy 2"))
maps.append((Map.from_yaml('tests/medium_map1.yaml'), "medium 1"))
maps.append((Map.from_yaml('tests/medium_map2.yaml'), "medium 2"))
maps.append((Map.from_yaml('tests/hard_map1.yaml'), "hard 1"))
maps.append((Map.from_yaml('tests/hard_map2.yaml'), "hard 2"))
maps.append((Map.from_yaml('tests/large_map1.yaml'), "large 1"))
maps.append((Map.from_yaml('tests/large_map2.yaml'), "large 2"))
maps.append((Map.from_yaml('tests/super_hard_map1.yaml'), "super hard"))
map_names = ["easy_1", "easy_2", "medium_1", "medium_2", "hard_1", "hard_2", "large_1", "large_2", "super_hard"]

# for map, name in maps:
#     start = time.time()
#     res, explored = ida(map, minimum_matching)
#     if res is True:
#         print("{0} was solved in {1} seconds & {2} states.".format(name, time.time()-start, explored))

# start = time.time()
# res, explored = beam_search(map1, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("easy 1 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map2, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("easy 2 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map3, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("medium 1 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map4, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("medium 2 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map5, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("hard 1 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map6, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("hard 2 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map7, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("large 1 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map8, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("large 2 was solved in: {0} seconds & {1} steps.".format(end, explored))

# start = time.time()
# res, explored = beam_search(map9, 5, minimum_matching)
# end = time.time() - start
# if res is True:
#     print("super hard was solved in: {0} seconds & {1} steps.".format(end, explored))

d = Map.from_str("_ X \n / P \n _ B \n _ _")
# d.plot_map()

# print(map4)
# m = "X _ _ _ _ \n _ _ X _ _ \n/ _ B _ / \n/ / _ _ _\n/ / B P /\n/ / X B _\n/ _ _ _ /\n/ _ _ _ _"
# d = Map.from_str(m)
# d.plot_map()

# FOR PLOTTING

# ida_states = []
# ida_time = []
# ida_undo = []

# for map, name in maps:
#     start = time.time()
#     res, explored, undo = ida(map, minimum_matching)
#     end = time.time()
#     if res is True:
#         print("{0} was solved in {1} seconds & {2} states.".format(name, end-start, explored))
#         ida_states.append(explored)
#         ida_time.append(end-start)
#         ida_undo.append(undo)
#     else: 
#         print(name + " was not solved.")
#         ida_states.append(0)
#         ida_time.append(0)
#         ida_undo.append(0)

# beam_states = []
# beam_time = []
# beam_undo = []

# for map, name in maps:
#     start = time.time()
#     res, explored, undo = beam_search(map, 90, minimum_matching)
#     end = time.time()
#     if res is True:
#         print("{0} was solved in {1} seconds & {2} states.".format(name, end-start, explored))
#         beam_states.append(explored)
#         beam_time.append(end-start)
#         beam_undo.append(undo)
#     else:
#         print(name + " was not solved.")
#         beam_states.append(0)
#         beam_time.append(0)
#         beam_undo.append(0)

# df = pd.DataFrame({
#     'Beam search explored states': map_names,
#     'States': beam_states
# })
# df.plot(x='Beam search explored states', y='States', kind="bar")
# plt.show()

# df = pd.DataFrame({
#     'Beam search completion time': map_names,
#     'Time (sec)': beam_time
# })
# df.plot(x='Beam search completion time', y='Time (sec)', kind="bar", logy=True)
# plt.show()

# df = pd.DataFrame({
#     'IDA* explored states': map_names,
#     'States': ida_states
# })
# df.plot(x='IDA* explored states', y='States', kind="bar", logy=True)
# plt.show()

# df = pd.DataFrame({
#     'IDA* completion time': map_names,
#     'Time (sec)': ida_time
# })
# df.plot(x='IDA* completion time', y='Time (sec)', kind="bar", logy=True)
# plt.show()

# cf = pd.DataFrame({
#     'Beam search cost': map_names,
#     'Number of pull moves': beam_undo
# })
# cf.plot(x='Beam search cost', y='Number of pull moves', kind='bar')
# plt.show()

# cf = pd.DataFrame({
#     'IDA* cost': map_names,
#     'Number of pull moves': ida_undo
# })
# cf.plot(x='IDA* cost', y='Number of pull moves', kind='bar')
# plt.show()
