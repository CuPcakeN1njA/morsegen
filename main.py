# -*- coding: latin-1 -*-

import sys
index = "abcdefghijklmnopqrstuvwxyz"
alph = [10111, # a
	111010101, # b
	11101011101, # c
	1110101, # d
	1, # e
	101011101, # f
	111011101, # g
	1010101, # h
	101, # i
	1011101110111, # j
	111010111, # k
	101110101, # l
	1110111, # m
	11101, # n
	11101110111, # o
	10111011101, # p
	1110111010111, # q
	1011101, # r
	10101, # s
	111, # t
	1010111, # u
	101010111, # v
	101110111, # w
	11101010111, # x
	1110101110111, # y
	11101110101 # z
	]

if __name__ == "__main__":
	sys.stdout.write("\033[1;31m[x]\033[1;m Input: ")
	word = raw_input()
	sys.stdout.write("\033[1;31m[x]\033[1;m Morse: ")
	for i in word:
		t = index.find(i)
		if((i != " ") and (t > 0)):
		#sys.stdout.write(str(alph[t-1]).replace("111", "███").replace("0", " ").replace("1", "•") + "   ")
			sys.stdout.write(str(alph[t]).replace("111", "███").replace("0", " ").replace("1", "█") + "   ")
		elif(i == " "):
			sys.stdout.write("       ")
		else:
			sys.stdout.write("")
	sys.stdout.write("\n")
	sys.stdout.flush()
