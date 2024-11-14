import pyautogui as pyg 
import keyboard
import sys
import time
from os import listdir







def screenshot_loop(mob):
	i = 1
	if listdir(f'.\\dataset\\{mob}'):
		i = max([int(file.split('.')[0]) for file in listdir(f'.\\dataset\\{mob}')])+1

	time.sleep(3)
	print('Starting...')
	while True:
		pyg.screenshot(f'.\\dataset\\{mob}\\{i}.png')
		i+=1
		if keyboard.is_pressed("q"):
			print("Ending loop")
			break
		else: time.sleep(1)


if __name__ == '__main__':
	print(sys.argv)
	if len(sys.argv) < 2:
		print('add argument to decide help')
		sys.exit()
	help_arg = sys.argv[1]

	if help_arg == 'screenshot':
		mob_arg = None
		try:
			mob_arg = sys.argv[2]
		except IndexError:
			print('add argument to decide mob')
			sys.exit()

		screenshot_loop(mob_arg)


	else:
		print('argument doesn\'t match any commands')