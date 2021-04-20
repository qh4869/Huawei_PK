#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys

player0_profit = []
player1_profit = []

def get_profit(input_lines):
	for line in input_lines:
		value = line.strip().split()
		if len(value)==5 and value[0]=='player0' and value[1]=='player1(Current':
			player0_profit.append(int(value[3]))
			player1_profit.append(int(value[4]))


def main(argv):
	with open(argv[1], 'r') as file:
		input_lines = file.readlines()

	get_profit(input_lines)

	plt.figure()
	plt.plot(player0_profit, color='red', label='player0')
	plt.plot(player1_profit, color='blue', label='player1')
	plt.legend()
	plt.show()

if __name__ == '__main__':
	main(sys.argv)