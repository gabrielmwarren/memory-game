from random import randint
from os import system
from time import sleep
import colorama
from colorama import Fore
colorama.init(autoreset=True)

nums = []
row1 = []
row2 = []
row3 = []
score = 0

print("I'm going to show you 9 numbers and you have 20 seconds to try to remember them in order")

sleep(2)


def get_nums(nums, row1, row2, row3):
    for i in range(3):
        nums.append(row1[i])
    for i in range(3):
        nums.append(row2[i])
    for i in range(3):
        nums.append(row3[i])


def get_rows(row1, row2, row3):
    for i in range(3):
        row1.append(randint(0, 9))
        row2.append(randint(0, 9))
        row3.append(randint(0, 9))


def quiz(nums, score):
    for i in range(9):
        answer = input('what is number ' + str(i) + ' ')
        if int(answer) == nums[i]:
            print('you got it right')
            score += 1
        else:
            print('Wrong It realy was ' + str(nums[i]))
    print('Your score was ' + str(score))


get_rows(row1, row2, row3)
get_nums(nums, row1, row2, row3)
print('Your numbers are')
print(Fore.RED + str(row1))
print(Fore.GREEN + str(row2))
print(Fore.MAGENTA + str(row3))

sleep(20)

system('clear')

quiz(nums, score)
