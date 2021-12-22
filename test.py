# Task 3
import json
from rtree import index


# Opening the ITN data as a dictionary
user = (440000, 87000)
dest = (400000, 90000)
with open('/Users/jiayuchen/Desktop/Material/itn/solent_itn.json') as file:
    itn_dict = json.load(file)
# Creating an index and adding each node's data to the index
idx = index.Index()
for i, node in enumerate(itn_dict['roadnodes'].items()):
    idx.insert(i, (node[1]['coords'][0], node[1]['coords'][1]), obj=node[0])
# # Assigning the two variables to empty strings to deal with a PEP8 notification
nearest_to_user = ''
nearest_to_dest = ''
# Identifying the nearest node to the user and destination
for i in idx.nearest((user[0], user[1]), 1, objects='raw'):
    nearest_to_user = i, itn_dict['roadnodes'][i]['coords']
for i in idx.nearest((dest[0], dest[1]), 1, objects='raw'):
    nearest_to_dest = i, itn_dict['roadnodes'][i]['coords']
# Avoiding empty paths from trying to be plotted
if nearest_to_user == nearest_to_dest:
    print('No paths available for the searched area, quitting.')
    quit()
print(nearest_to_dest, nearest_to_user)

# Creating the connections between the user and destination's locations
# and their respective nearest nodes (to be plotted)
# user_to_node = LineString([(user.x, user.y), (nearest_to_user[1][0], nearest_to_user[1][1])])
# node_to_dest = LineString([(nearest_to_dest[1][0], nearest_to_dest[1][1]), (dest.x, dest.y)])