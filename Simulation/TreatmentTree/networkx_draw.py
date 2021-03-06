import matplotlib.pyplot as plt
import networkx as nx
import random
from .node import Node

def __create_branch(G:nx.Graph, nodes:list[Node]):
    for i in range(len(nodes)):
        G.add_node(nodes[i].name)
        if i > 0:
            G.add_edge(nodes[i].name, nodes[i-1].name)

def __create_graph(G:nx.Graph,nodes:list[Node], n):
    if len(nodes) == 0 or n == 0:
        return
    for node in nodes:
        if node is not None:
            val = node.name
            G.add_node(val)
            if node.parent != None:
                G.add_edge(node.parent.name, val)
    childrens = []
    for node in nodes:
        if node is not None:
            childrens.extend(node._children)
    __create_graph(G, childrens, n-1)

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 
    
    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.
    
    G: the graph (must be a tree)
    
    root: the root node of current branch 
    - if the tree is directed and this is not given, 
    the root will be found and used
    - if the tree is directed and this is given, then 
    the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
    then a random choice will be used.
    
    width: horizontal space allocated for this branch - avoids overlap with other branches
    vert_gap: gap between levels of hierarchy
    vert_loc: vertical location of root
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed
        '''
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def visualize_graph_nx(root:Node, level):
    G = nx.Graph()
    __create_graph(G, [root], level)
    pos = hierarchy_pos(G,f"-1 :0")    
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
    #plt.figure(figsize=(16,16))
    plt.show()

def visualize_branch_nx(branch_nodes:list[Node]):
    G = nx.Graph()
    __create_branch(G, branch_nodes)
    pos = hierarchy_pos(G,f"-1 :0")    
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
    #plt.figure(figsize=(16,16))

    plt.show()

def print_console_nodes(nodes:list[Node], n):
    if n== 0 or len(nodes) == 0:
        return
    for node in nodes:
        if node is not None:
            val = node.name ##node.value if node.value!="" else str(n)
            print(val, end="  ")
    print()
    children = []
    for node in nodes:
        if node is not None:
            children.extend(node._children)
    print_console_nodes(children,n-1)