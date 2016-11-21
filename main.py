# Coded by Naoto Hayashi
# coding: UTF-8

from def_class import *
from def_data import *
from def_minFlow import *
import sys
sys.setrecursionlimit(20000)

import numpy as np
import matplotlib.pyplot as plt

flowRoot = TaskInFlow([], None, root)
MakeTaskStFlow(flowRoot, s)

'''
print "======"
print flowRoot.task.prob
print flowRoot.task.lev
print flowRoot.task.thing
print flowRoot.depth
print "======"
print flowRoot.children[0].st.lev
print flowRoot.children[0].st.thing
print flowRoot.children[0].st.cost
print flowRoot.children[0].depth
print "------"
print flowRoot.children[1].st.lev
print flowRoot.children[1].st.thing
print flowRoot.children[1].st.cost
print flowRoot.children[1].depth
print "------"
print flowRoot.children[2].st.lev
print flowRoot.children[2].st.thing
print flowRoot.children[2].st.cost
print flowRoot.children[2].depth
print "------"
print flowRoot.children[3].st.lev
print flowRoot.children[3].st.thing
print flowRoot.children[3].st.cost
print flowRoot.children[3].depth
print "======"
print flowRoot.children[0].children[0].task.prob
print flowRoot.children[0].children[0].task.lev
print flowRoot.children[0].children[0].task.thing
print flowRoot.children[0].children[0].depth
print "------"
print flowRoot.children[0].children[1].task.prob
print flowRoot.children[0].children[1].task.lev
print flowRoot.children[0].children[1].task.thing
print flowRoot.children[0].children[1].depth
print "------"
print flowRoot.children[1].children[0].task.prob
print flowRoot.children[1].children[0].task.lev
print flowRoot.children[1].children[0].task.thing
print flowRoot.children[1].children[0].depth
print "------"
print flowRoot.children[2].children[0].task.prob
print flowRoot.children[2].children[0].task.lev
print flowRoot.children[2].children[0].task.thing
print flowRoot.children[2].children[0].depth
print "------"
print flowRoot.children[3].children
print "======"
print flowRoot.children[0].children[0].children
print "------"
print flowRoot.children[0].children[0].children[0].st.lev
print flowRoot.children[0].children[0].children[0].st.thing
print flowRoot.children[0].children[0].children[0].st.cost
print flowRoot.children[0].children[0].children[0].depth
print "------"
print flowRoot.children[0].children[0].children[1].st.lev
print flowRoot.children[0].children[0].children[1].st.thing
print flowRoot.children[0].children[0].children[1].st.cost
print flowRoot.children[0].children[0].children[1].depth
print "------"
print flowRoot.children[0].children[1].children
print "------"
print flowRoot.children[0].children[1].children[0].st.lev
print flowRoot.children[0].children[1].children[0].st.thing
print flowRoot.children[0].children[1].children[0].st.cost
print flowRoot.children[0].children[1].children[0].depth
print "------"
print flowRoot.children[0].children[1].children[1].st.lev
print flowRoot.children[0].children[1].children[1].st.thing
print flowRoot.children[0].children[1].children[1].st.cost
print flowRoot.children[0].children[1].children[1].depth
print "------"
print flowRoot.children[1].children[0].children
print "------"
print flowRoot.children[1].children[0].children[0].st.lev
print flowRoot.children[1].children[0].children[0].st.thing
print flowRoot.children[1].children[0].children[0].st.cost
print flowRoot.children[1].children[0].children[0].depth
print "------"
print flowRoot.children[1].children[0].children[1].st.lev
print flowRoot.children[1].children[0].children[1].st.thing
print flowRoot.children[1].children[0].children[1].st.cost
print flowRoot.children[1].children[0].children[1].depth
print "------"
print flowRoot.children[2].children[0].children
print "------"
print flowRoot.children[2].children[0].children[0].st.lev
print flowRoot.children[2].children[0].children[0].st.thing
print flowRoot.children[2].children[0].children[0].st.cost
print flowRoot.children[2].children[0].children[0].depth
print "------"
print flowRoot.children[2].children[0].children[1].st.lev
print flowRoot.children[2].children[0].children[1].st.thing
print flowRoot.children[2].children[0].children[1].st.cost
print flowRoot.children[2].children[0].children[1].depth
print "======"
print flowRoot.children[0].children[0].children[0].children
print flowRoot.children[0].children[0].children[1].children
print flowRoot.children[0].children[1].children[0].children
print flowRoot.children[0].children[1].children[1].children
print flowRoot.children[1].children[0].children[0].children
print flowRoot.children[1].children[0].children[1].children
print flowRoot.children[2].children[0].children[0].children
print flowRoot.children[2].children[0].children[1].children
print "======"
print flowRoot.children[0].children[1].children[0].children[0].task.prob
print flowRoot.children[0].children[1].children[0].children[0].task.lev
print flowRoot.children[0].children[1].children[0].children[0].task.thing
print flowRoot.children[0].children[1].children[0].children[0].children

print flowRoot.children[0].children[1].children[0].children[0].children[0].children

print flowRoot.children[0].children[1].children[0].children[0].children[1].children
'''

leaves = []
getLeaves(flowRoot, leaves) #flow_nodeの葉ノードを集める関数	
# leaves = [(node1), (node2), ....]
#print leaves

#print deepestLeaf(leaves)
#print exist(flowRoot, leaves)
MakeMinCostFlow(leaves, deepestLeaf(leaves)) #flowRootには選別された木構造のみ残る


def print_flow(flow_node):
	print "タスク[ 確率: %f, レベル: %d, パーツ: %s ], 戦略 [ コスト: %d, レベル: %d, パーツ: %s ]" % (flow_node.task.prob, flow_node.task.lev, flow_node.task.thing, flow_node.children.st.cost, flow_node.children.st.lev, flow_node.children.st.thing)
	if flow_node.children.children != []:
		for child in flow_node.children.children:
			print_flow(child)
	else:
		return

print_flow(flowRoot)
'''
print "======"
print flowRoot.task.prob
print flowRoot.task.lev
print flowRoot.task.thing
print flowRoot.depth
print flowRoot.c
print "======"
print flowRoot.children.st.lev
print flowRoot.children.st.thing
print flowRoot.children.st.cost
print flowRoot.children.depth
print flowRoot.children.c
print "======"
print flowRoot.children.children
print flowRoot.children.children[0].task.prob
print flowRoot.children.children[0].task.lev
print flowRoot.children.children[0].task.thing
print flowRoot.children.children[0].depth
print "------"
print flowRoot.children.children[1].task.prob
print flowRoot.children.children[1].task.lev
print flowRoot.children.children[1].task.thing
print flowRoot.children.children[1].depth
print "======"
print flowRoot.children.children[0].children
print flowRoot.children.children[1].children
print "------"
print flowRoot.children.children[0].children.st.lev
print flowRoot.children.children[0].children.st.thing
print flowRoot.children.children[0].children.st.cost
print flowRoot.children.children[0].children.depth
print "------"
print flowRoot.children.children[1].children.st.lev
print flowRoot.children.children[1].children.st.thing
print flowRoot.children.children[1].children.st.cost
print flowRoot.children.children[1].children.depth
'''

#パラメータを動かした時のグラフ出力
#x = np.arange(-3, 3, 0.1)
#y = np.sin(x)
#plt.plot(x, y)
#plt.show()'''