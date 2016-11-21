# Coded by Naoto Hayashi
# coding: UTF-8

from def_class import * 

def isLeaf(flow_node): #flow_nodeが葉ノードか確かめる関数
	return flow_node.children == [] or flow_node.children is None

def getLeaves(flow_node, Leaves): #flow_nodeの葉ノードを集める関数	
	if isLeaf(flow_node):
		flow_node.c = flow_node.st.cost
		Leaves.append(flow_node)
		return

	for child in flow_node.children:
		getLeaves(child, Leaves)

	return

def deepestLeaf(Leaves):
	max_depth = Leaves[0].depth
	for leaf in Leaves:
		if max_depth < leaf.depth:
			max_depth = leaf.depth 

	return max_depth

#nodesの中にflow_nodesはあるか？ある:：False、ない：True
def exist(flow_node, nodes):
	for node in nodes:
		if node == flow_node:
			return False

	return True

def MakeMinCostFlow(current_leaves, cur_depth):

	next_leaves = []
	for leaf in current_leaves: #深さcur_depthにおいて、選別を行う
		ChooseChild(leaf, cur_depth)

		if leaf.depth == cur_depth:
			if leaf.parent is not None and exist(leaf.parent, next_leaves): #親leaf.parentがあって、next_leavesにすでに含まれていない場合
				next_leaves.append(leaf.parent)

		else:
			next_leaves.append(leaf)

	if cur_depth != 0:
		MakeMinCostFlow(next_leaves, cur_depth - 1)	
	
	return

#ある深さcur_depthにおいて、flow_nodeの兄弟で選別を行う
def ChooseChild(flow_node, cur_depth):
	if flow_node.depth == cur_depth and flow_node.parent is not None: #深さ・親・兄弟確認
		if isinstance(flow_node, TaskInFlow): #TaskInFlowの場合
			if flow_node == flow_node.parent.children[0]:
				SumTaskFlow(flow_node) #TaskInFlowの兄弟タスク(TaskInFlow)のコストの和
			return
		else: #StInFlowの場合
			CompStFlow(flow_node) #StInFlowの兄弟タスク(StInFlow)の最安のものを選別
			return
	else: #葉っぱから消す場合と消さない場合注意
		return

#TaskInFlowの兄弟タスク(TaskInFlow)のコストの和
def SumTaskFlow(TIF):
	assert isinstance(TIF, TaskInFlow)
	for child in TIF.parent.children:
		TIF.parent.c += child.c

	TIF.parent.c += TIF.parent.st.cost
	return

#StInFlowの兄弟タスク(StInFlow)の最安のものを選別
def CompStFlow(SIF):
	assert isinstance(SIF, StInFlow)

	if SIF.parent is not None:
		if isinstance(SIF.parent.children, StInFlow):
			min_SIF = SIF.parent.children
		else:
			min_SIF = SIF.parent.children[0]
			for child in SIF.parent.children:
				if min_SIF.c > child.c:
#					min_SIF.parent = None
					min_SIF = child #最安の兄弟をmin_cost_SIFにセット
#				else:
#					child.parent = None
				
		SIF.parent.children = min_SIF #最安の兄弟以外を親から切り離す
		SIF.parent.c = min_SIF.c * SIF.parent.task.prob

	return
