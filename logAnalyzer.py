#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys

player0_profit = []
player1_profit = []
player0_income = [] # 收入
player1_income = []
player0_req = [] # 成功交易次数
player1_req = []

def get_profit(input_lines):
	for line in input_lines:
		value = line.strip().split()
		if len(value)==5 and value[0]=='player0' and value[1]=='player1(Current':
			player0_profit.append(int(value[3]))
			player1_profit.append(int(value[4]))


def get_income_and_req(input_lines):
	for line in input_lines:
		value = line.strip().split(' ')
		if len(value)==2 and value[0]=='Day':
			daily_income_0 = 0
			daily_income_1 = 0
			daily_req_0 = 0
			daily_req_1 = 0
		elif len(value)==2:
			val0 = value[0].split(',')
			val1 = value[1].split(',')


			value_0 = int(val0[0])
			value_1 = int(val1[0])

			if len(val0) > 1 and len(val1) > 1:
				if value_0 == -1 and value_1 == -1:
					succ_0 = False
					succ_1 = False
				elif value_0 == -1 and value_1 != -1:
					succ_0 = False
					succ_1 = True
				elif value_0 != -1 and value_1 == -1:
					succ_0 = True
					succ_1 = False
				elif value_0 < value_1:
					succ_0 = True
					succ_1 = False
				elif value_0 > value_1:
					succ_0 = False
					succ_1 = True
				else:
					succ_0 = True
					succ_1 = True
			elif len(val0) > 1 and len(val1) == 1:
				succ_0 = True
				succ_1 = False
			elif len(val1) > 1 and len(val0) == 1:
				succ_0 = False
				succ_1 = True
			else:
				if value_0 == -1 and value_1 == -1:
					succ_0 = False
					succ_1 = False
				elif value_0 == -1 and value_1 != -1:
					succ_0 = False
					succ_1 = True
				elif value_0 != -1 and value_1 == -1:
					succ_0 = True
					succ_1 = False
				elif value_0 < value_1:
					succ_0 = True
					succ_1 = False
				elif value_0 > value_1:
					succ_0 = False
					succ_1 = True
				else:
					succ_0 = True
					succ_1 = True

			if succ_0:
				daily_income_0 += value_0
				daily_req_0 += 1

			if succ_1:
				daily_income_1 += value_1
				daily_req_1 += 1

		elif len(value)==5 and value[0]=='player0' and value[1]=='player1(Current':
			# if player0_income and player1_income:
			# 	player0_income.append(player0_income[-1] + daily_income_0)
			# 	player1_income.append(player1_income[-1] + daily_income_1)
			# 	player0_req.append(player0_req[-1] + daily_req_0)
			# 	player1_req.append(player1_req[-1] + daily_req_1)
			# else:
				player0_income.append(daily_income_0)
				player1_income.append(daily_income_1)
				player0_req.append(daily_req_0)
				player1_req.append(daily_req_1)


def main(argv):
	with open(argv[1], 'r') as file:
		input_lines = file.readlines()

	get_profit(input_lines)
	get_income_and_req(input_lines)

	plt.figure()
	plt.plot(player0_profit, color='red', label='player0',alpha=0.7)
	plt.plot(player1_profit, color='blue', label='player1',alpha=0.7)
	plt.title('Total profit')
	plt.legend()

	plt.figure()
	plt.plot(player0_income, color='red', label='player0', alpha=0.7, zorder=1)
	plt.plot(player1_income, color='blue', label='player1', alpha=0.7, zorder=0)
	plt.title('Income Each Day')
	plt.legend()

	plt.figure()
	plt.plot(player0_req, color='red', label='player0',alpha=0.7)
	plt.plot(player1_req, color='blue', label='player1',alpha=0.7)
	plt.title('Obtained Req. Each Day')
	plt.legend()

	plt.show()

if __name__ == '__main__':
	main(sys.argv)