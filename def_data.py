# Coded by Naoto Hayashi
# coding: UTF-8

from def_class import * 

#ストラテジーのインスタンスのタプル生成
VILLEGE = 500 #農村部の人の人件費
URBAN = 10000 #都市部の人の人件費
THING_A = 1000 #Aのパーツ経費
THING_B = 5000 #Bのパーツ経費
THING_C = 5000 #Cのパーツ経費
THING_D = 1000 #Dのパーツ経費
THING_E = 3000 #Eのパーツ経費

s = [St(0, [], VILLEGE), 
	St(0, ['A'], VILLEGE+THING_A),
	St(0, ['B'], VILLEGE+THING_B),
	St(0, ['A', 'B', 'C'], VILLEGE+THING_A+THING_B+THING_C)
	]
'''
s = [St(0, [], VILLEGE), 
	St(0, ['A'], VILLEGE+THING_A),
	St(0, ['B'], VILLEGE+THING_B),
	St(0, ['C'], VILLEGE+THING_C),
	St(0, ['D'], VILLEGE+THING_D),
	St(0, ['E'], VILLEGE+THING_E),
	St(0, ['A', 'B'], VILLEGE+THING_A+THING_B),
	St(0, ['A', 'C'], VILLEGE+THING_A+THING_C),
	St(0, ['A', 'D'], VILLEGE+THING_A+THING_D),
	St(0, ['A', 'E'], VILLEGE+THING_A+THING_E),
	St(0, ['B', 'C'], VILLEGE+THING_B+THING_C),
	St(0, ['B', 'D'], VILLEGE+THING_B+THING_D),
	St(0, ['B', 'E'], VILLEGE+THING_B+THING_E),
	St(0, ['C', 'D'], VILLEGE+THING_C+THING_D),
	St(0, ['C', 'E'], VILLEGE+THING_C+THING_E),
	St(0, ['D', 'E'], VILLEGE+THING_D+THING_E),
	St(0, ['A', 'B', 'C'], VILLEGE+THING_A+THING_B+THING_C),
	St(0, ['A', 'B', 'D'], VILLEGE+THING_A+THING_B+THING_D),
	St(0, ['A', 'B', 'E'], VILLEGE+THING_A+THING_B+THING_E),
	St(0, ['A', 'C', 'D'], VILLEGE+THING_A+THING_C+THING_D),
	St(0, ['A', 'C', 'E'], VILLEGE+THING_A+THING_C+THING_E),
	St(0, ['A', 'D', 'E'], VILLEGE+THING_A+THING_D+THING_E),
	St(0, ['B', 'C', 'D'], VILLEGE+THING_B+THING_C+THING_D),
	St(0, ['B', 'C', 'E'], VILLEGE+THING_B+THING_C+THING_E),
	St(0, ['B', 'D', 'E'], VILLEGE+THING_B+THING_D+THING_E),
	St(0, ['C', 'D', 'E'], VILLEGE+THING_C+THING_D+THING_E),
	St(0, ['A', 'B', 'C', 'D'], VILLEGE+THING_A+THING_B+THING_C+THING_D),
	St(0, ['A', 'B', 'C', 'E'], VILLEGE+THING_A+THING_B+THING_C+THING_E),
	St(0, ['A', 'B', 'D', 'E'], VILLEGE+THING_A+THING_B+THING_D+THING_E),
	St(0, ['A', 'C', 'D', 'E'], VILLEGE+THING_A+THING_C+THING_D+THING_E),
	St(0, ['B', 'C', 'D', 'E'], VILLEGE+THING_B+THING_C+THING_D+THING_E),
	St(0, ['A', 'B', 'C', 'D', 'E'], VILLEGE+THING_A+THING_B+THING_C+THING_D+THING_E),
	St(1, [], URBAN), 
	St(1, ['A'], URBAN+THING_A),
	St(1, ['B'], URBAN+THING_B),
	St(1, ['C'], URBAN+THING_C),
	St(1, ['D'], URBAN+THING_D),
	St(1, ['E'], URBAN+THING_E),
	St(1, ['A', 'B'], URBAN+THING_A+THING_B),
	St(1, ['A', 'C'], URBAN+THING_A+THING_C),
	St(1, ['A', 'D'], URBAN+THING_A+THING_D),
	St(1, ['A', 'E'], URBAN+THING_A+THING_E),
	St(1, ['B', 'C'], URBAN+THING_B+THING_C),
	St(1, ['B', 'D'], URBAN+THING_B+THING_D),
	St(1, ['B', 'E'], URBAN+THING_B+THING_E),
	St(1, ['C', 'D'], URBAN+THING_C+THING_D),
	St(1, ['C', 'E'], URBAN+THING_C+THING_E),
	St(1, ['D', 'E'], URBAN+THING_D+THING_E),
	St(1, ['A', 'B', 'C'], URBAN+THING_A+THING_B+THING_C),
	St(1, ['A', 'B', 'D'], URBAN+THING_A+THING_B+THING_D),
	St(1, ['A', 'B', 'E'], URBAN+THING_A+THING_B+THING_E),
	St(1, ['A', 'C', 'D'], URBAN+THING_A+THING_C+THING_D),
	St(1, ['A', 'C', 'E'], URBAN+THING_A+THING_C+THING_E),
	St(1, ['A', 'D', 'E'], URBAN+THING_A+THING_D+THING_E),
	St(1, ['B', 'C', 'D'], URBAN+THING_B+THING_C+THING_D),
	St(1, ['B', 'C', 'E'], URBAN+THING_B+THING_C+THING_E),
	St(1, ['B', 'D', 'E'], URBAN+THING_B+THING_D+THING_E),
	St(1, ['C', 'D', 'E'], URBAN+THING_C+THING_D+THING_E),
	St(1, ['A', 'B', 'C', 'D'], URBAN+THING_A+THING_B+THING_C+THING_D),
	St(1, ['A', 'B', 'C', 'E'], URBAN+THING_A+THING_B+THING_C+THING_E),
	St(1, ['A', 'B', 'D', 'E'], URBAN+THING_A+THING_B+THING_D+THING_E),
	St(1, ['A', 'C', 'D', 'E'], URBAN+THING_A+THING_C+THING_D+THING_E),
	St(1, ['B', 'C', 'D', 'E'], URBAN+THING_B+THING_C+THING_D+THING_E),
	St(1, ['A', 'B', 'C', 'D', 'E'], URBAN+THING_A+THING_B+THING_C+THING_D+THING_E)
	]
'''

# タスクフローの木構造生成
#高頻度	0.2325	4つ
#低頻度	0.01	7つ
'''root = Task(1.0, 0, [], True, [
   	Task(0.2625, 0, [], True, [
   		Task(0.01, 0, [], True, []),
   		Task(0.2525, 0, [], True, [
			Task(0.01, 0, [], True, []),
			Task(0.2425, 1, 'A', True, [
				Task(0.2325, 0, [], True, []),
				Task(0.01, 1, 'B', True, [])
			])
		])
	]), 
	Task(0.7375, 0, [], True, [
		Task(0.2625, 0, [], True, [
			Task(0.2425, 0, [], True, [
				Task(0.2325, 0, [], True, []),
				Task(0.01, 1, 'C', True, [])
			]),
			Task(0.02, 0, [], True, [
				Task(0.01, 1, 'D', True, []),
				Task(0.01, 1, [], True, [])
			])
		]),
		Task(0.475, 0, [], True, [
			Task(0.01, 1, [], True, []),
			Task(0.465, 1, [], True, [
				Task(0.2325, 1, 'E', True, []),
				Task(0.2325, 0, [], True, [])
			])
		])	
	])
])'''


root = Task(1.0, 0, [], True, [
	Task(0.8, 0, 'B', True, []),
	Task(0.2, 0, 'A', True, [])
])
