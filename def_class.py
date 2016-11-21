# Coded by Naoto Hayashi
# coding: UTF-8

DEFAULT = 10000000

#タスクノードのクラスTaskを定義
class Task(object):
	def __init__(self, prob, lev, thing, flag, children):
		self.prob = prob
		self.lev = lev
		self.thing = thing
		self.flag = flag
		self.children = children
		self.parent = None

		if children != []:
			for child in children:
				child.parent = self

 #   	if children is not None:
 #		   	assert sum([child.prob for child in children]) == 1.0

	def is_leaf(self):
		if self.children == []:
			return True
		else:
			return False

#ストラテジーのクラスStを定義
class St(object):
	def __init__(self, lev, thing, cost):
		self.lev = lev
		self.thing = thing
		self.cost = cost

#取るべきストラテジーとタスクノードの木構造のクラスを定義
class TaskInFlow(object):
	def __init__(self, children, parent, task):
		self.children = children #StInFlowクラスのオブジェクトリスト
		self.parent = parent #StInFlowクラス	
		self.task = task #Taskクラス

		self.c = 0
		self.depth = 0

	def setChildren_st(self, children_st): #children_stはStクラスのリスト		
		for st in children_st:		
			self.children.append(StInFlow([], None, st))
		for child in self.children:
			child.parent = self
			child.depth = self.depth + 1

class StInFlow(object):
	def __init__(self, children, parent, st):
		self.children = children #TaskInFlowクラスのオブジェクトリスト
		self.parent = parent #TaskInFlowクラス
		self.st = st #Stクラス

		self.c = 0
		self.depth = 0

	def setChildren_task(self, children_task):
		for task in children_task: #Task型
			self.children.append(TaskInFlow([], None, task))
		for child in self.children:
	   		child.parent = self 
	   		child.depth = self.depth + 1

def MakeTaskStFlow(TIF, Strategies): #インスタンスTIFはTaskInFlowクラス

	TIF.task.flag = False

	st_list = []
	findThoughSt(TIF, Strategies, st_list)
	TIF.setChildren_st(st_list)
	
	for sif in TIF.children:
		task_list = []
		findStuckTask(TIF.task, TIF.task, sif, task_list) #このメソッドがflagを変える
		
		if task_list != []:
			sif.setChildren_task(task_list) #Taskを追加

			for tif in sif.children:
				MakeTaskStFlow(tif, Strategies)
		
		resetFlag(TIF.task)

	return

#Strategiesから、タスクノード（TIF.task）を突破できるストラテジーchildrenを洗い出すメソッド
def findThoughSt(TIF, Strategies, children_st): #StrategiesはStクラスのリスト

	for st in Strategies:
		if Comp(TIF.task, st):
			children_st.append(st)

	return

#タスクノードTから始めたとき、ストラテジー（SIF.st）が突破できず引っかかるタスクノードchildrenを洗い出すメソッド	
def findStuckTask(T1, T, SIF, children_task): #TはTaskクラスのインスタンス

	if Comp(T1, SIF.st):
		if CheckNext(T1, T) is not None:
			findStuckTask(JumpNext(T1, T), T, SIF, children_task)
			return
		else:
			return 
	else:
		children_task.append(T1) #SIF.stで突破できないTを追加
		if CheckNext(T1.parent, T) is not None:
			findStuckTask(JumpNext(T1.parent, T), T, SIF, children_task)
			return
		else:
			return

#タスクノード（T）をストラテジー（Strategy）で突破できるか判定するメソッド
def Comp(T, Strategy): 

	if T.thing == []:
		return T.lev <= Strategy.lev

	elif T.thing in Strategy.thing and T.lev <= Strategy.lev: 
		return True

	else:
		return False

#あるノードT以下における探索で、T1の次のノードを検索するメソッド
def CheckNext(T1, T): 
	if T1.is_leaf() == True: #葉ノードの場合	
		if T1.parent != T.parent:
			return CheckNext(T1.parent, T)
		else:
			return

	else: #子ノードがある場合
		for child in T1.children:
			if child.flag:
				return child

		#子ノードはあるが、全てカウントされていた場合
		if T1.parent != None:
			if T1.parent != T.parent:
				return CheckNext(T1.parent, T)
			else:
				return

		#全てカウントされた場合
		else:
			return

#あるノードT以下における探索で、T1の次のノードにとぶメソッド
def JumpNext(T1, T):
	if CheckNext(T1, T) is not None:
		Next = CheckNext(T1, T)
		Next.flag = False
		return Next
		
	else:
		return

#ナメたタスクノードをリセットするメソッド
def resetFlag(T):
	T.flag = True 
	if T.is_leaf() != True:
		for child in T.children:
			resetFlag(child)

	else:
		return

def checkBelowFlags(T, count): #TはTaskクラスのインスタンス
	if T.flag == True:
		count += 1 

	if T.is_leaf():
		return count

	else:
		for child in T.children:
			count = checkBelowFlags(child, count)
		
		return count