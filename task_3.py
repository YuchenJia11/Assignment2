# Task 3
import json
import rtree.index


def read_json(file):
    with open(file) as json_file:
        dict = json.load(json_file)
    return (dict)


def read_nodes(file):
    dict = read_json(file)
    roadnodes = list(dict['roadnodes'].items())
    # a roadnode example: 'osgb4000000026126626': {'coords': [447798.467, 80320.178]}
    return (roadnodes)


def itn(user, highest_point, itn_path):
    node_list = []
    if_samepoint = False
    roadnodes = read_nodes(itn_path)
    idx = rtree.index.Rtree()
    for i, nodes in enumerate(roadnodes):
        node_list.append(nodes[1]['coords'])

    for i, nodes in enumerate(node_list):
        idx.insert(i, nodes+nodes, nodes)

    user_nearest_list = list(idx.nearest(user, 1, objects='raw'))
    nearest_user = user_nearest_list[0]
    hp_nearest_list = list(idx.nearest(highest_point, 1, objects='raw'))
    nearest_hp = hp_nearest_list[0]

    if nearest_user == nearest_hp:
        if_samepoint = True

    return nearest_user, nearest_hp, if_samepoint
