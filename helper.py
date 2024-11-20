import pyautogui as pyg 
import keyboard
import sys
import time
from os import listdir, getcwd, path
from PIL import Image 


#C:\Users\mbutl\Downloads\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=chickens_pos.txt --images=dataset\chickens\
# change slashes
# make negative files
#C:\Users\mbutl\Downloads\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info annotations\chickens_pos.txt -w 24 -h 24 -num 1000 -vec annotations\chicken_pos.vec
#C:\Users\mbutl\Downloads\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade\chicken -vec annotations\chickens_pos.vec -bg annotations\chickens_neg.txt -w 24 -h 24 -numPos 200 -numNeg 100 -numStages 10

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


def resize_images(dir_list,size=(1024,576)):
	for dir in dir_list:
		p = path.join(getcwd(),dir)
		for file in listdir(p):
			img = Image.open(path.join(p,file))
			img = img.resize(size)
			img.save(path.join(p,file))


def negative_files(pos_folder):
	cwd = f'dataset'
	for folder in listdir(cwd):
		if folder == pos_folder:
			continue
		

		p = path.join(cwd,folder)
		for file in listdir(p):
			with open(path.join('annotations',str(pos_folder)+'_neg.txt'), 'a') as f:
				f.write(path.join(p,file))
				f.write('\n')



if __name__ == '__main__':
	

	# STOPPAGE
	sys.exit()

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
	elif help_arg == 'resize_images':
		x = [path.join('dataset',folder) for folder in listdir('dataset')]
		resize_images(x)

	else:
		print('argument doesn\'t match any commands')