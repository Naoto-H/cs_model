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

#print_flow(flowRoot)

print flowRoot.c
#パラメータを動かした時のグラフ出力
x = np.arange(0, 10000)
THING_A = x
y = flowRoot.c
plt.plot(x, y)
plt.show()