# Coded by Naoto Hayashi
# coding: UTF-8

from def_class import *
from def_data import *
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
print "======"
print flowRoot.children[0].st.lev
print flowRoot.children[0].st.thing
print flowRoot.children[0].st.cost
print "------"
print flowRoot.children[1].st.lev
print flowRoot.children[1].st.thing
print flowRoot.children[1].st.cost
print "------"
print flowRoot.children[2].st.lev
print flowRoot.children[2].st.thing
print flowRoot.children[2].st.cost
print "------"
print flowRoot.children[3].st.lev
print flowRoot.children[3].st.thing
print flowRoot.children[3].st.cost
print "======"
print flowRoot.children[0].children[0].task.prob
print flowRoot.children[0].children[0].task.lev
print flowRoot.children[0].children[0].task.thing
print "------"
print flowRoot.children[0].children[1].task.prob
print flowRoot.children[0].children[1].task.lev
print flowRoot.children[0].children[1].task.thing
print "------"
print flowRoot.children[1].children[0].task.prob
print flowRoot.children[1].children[0].task.lev
print flowRoot.children[1].children[0].task.thing
print "------"
print flowRoot.children[2].children[0].task.prob
print flowRoot.children[2].children[0].task.lev
print flowRoot.children[2].children[0].task.thing
print "------"
print flowRoot.children[3].children
print "======"
print flowRoot.children[0].children[0].children
print "------"
print flowRoot.children[0].children[0].children[0].st.lev
print flowRoot.children[0].children[0].children[0].st.thing
print flowRoot.children[0].children[0].children[0].st.cost
print "------"
print flowRoot.children[0].children[0].children[1].st.lev
print flowRoot.children[0].children[0].children[1].st.thing
print flowRoot.children[0].children[0].children[1].st.cost
print "------"
print flowRoot.children[0].children[1].children
print "------"
print flowRoot.children[0].children[1].children[0].st.lev
print flowRoot.children[0].children[1].children[0].st.thing
print flowRoot.children[0].children[1].children[0].st.cost
print "------"
print flowRoot.children[0].children[1].children[1].st.lev
print flowRoot.children[0].children[1].children[1].st.thing
print flowRoot.children[0].children[1].children[1].st.cost
print "------"
print flowRoot.children[1].children[0].children
print "------"
print flowRoot.children[1].children[0].children[0].st.lev
print flowRoot.children[1].children[0].children[0].st.thing
print flowRoot.children[1].children[0].children[0].st.cost
print "------"
print flowRoot.children[1].children[0].children[1].st.lev
print flowRoot.children[1].children[0].children[1].st.thing
print flowRoot.children[1].children[0].children[1].st.cost
print "------"
print flowRoot.children[2].children[0].children
print "------"
print flowRoot.children[2].children[0].children[0].st.lev
print flowRoot.children[2].children[0].children[0].st.thing
print flowRoot.children[2].children[0].children[0].st.cost
print "------"
print flowRoot.children[2].children[0].children[1].st.lev
print flowRoot.children[2].children[0].children[1].st.thing
print flowRoot.children[2].children[0].children[1].st.cost
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

def isLeaf(flow_node):
	return flow_node.children == [] or flow_node.children is None

def getLeaves(flow_node): #期待値のコストを求める関数
	if isLeaf(flow_node):
		flow_node.flag = True
		leaves.append(flow_node)
		return

	for child in flow_node.children:
		getLeaves(child)

	return

getLeaves(flowRoot)
print leaves


def MakeMinCostFlow(TIF):
	CompStFlow(TIF)
	
	for sif in TIF.children:
		SumTaskFlow(sif)

		if isLeaf(sif) != True:
			for tif in sif.children:
				MakeMinCostFlow(tif)

	return

# leaves = [(node1), (node2), ....]
#print leaves
'''
for minLeaf

minLeaf = findMinLeaf(leaves)
# minLeaf = (node1, 400)

print minLeaf

minFlow = []

def extractMinFlow(flow_node):
	if flow_node != None:
		if isinstance(flow_node, StInFlow):
			minFlow.append([flow_node.parent, flow_node])

		extractMinFlow(flow_node.parent)

	return

extractMinFlow(minLeaf[0])
# minFlow = [ [task1, st1], [task2, st3], [task3, st5], ... ]

minFlow.reverse()

print minFlow

print minFlow[0][0].task.prob
print minFlow[0][0].task.lev
print minFlow[0][0].task.thing

print minFlow[0][1].st.lev
print minFlow[0][1].st.thing
print minFlow[0][1].st.cost

print minFlow[1][0].task.prob
print minFlow[1][0].task.lev
print minFlow[1][0].task.thing

print minFlow[1][1].st.lev
print minFlow[1][1].st.thing
print minFlow[1][1].st.cost
'''

#パラメータを動かした時のグラフ出力
#x = np.arange(-3, 3, 0.1)
#y = np.sin(x)
#plt.plot(x, y)
#plt.show()'''