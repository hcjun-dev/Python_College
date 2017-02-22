import src.file0123_1, src.file0123_2, src.file0128, src.file0130t
import src.file0205, src.file0206, src.file0211, src.file0213, src.file0220, src.file0225, src.file0227_1
import src.file0304, src.file0306, src.file0317, src.file0320, src.file0324, src.file0325
import src.file0401, src.file0410, src.file0414_1classStudent, src.file0414_2classCar,src.file0421, src.file0424




def helpOption():
	print('\nls - list of what files I have')
	print('dir - list of what files I have')
	print('help - display help')


def ls():
	print('\nJanuary - 01')
	print('0123_1\t0123_2\t0128\t0130t')
	print('\nFebruary - 02')
	print('0205\t0206\t0211\t0213\t0220\t0225\t0227_1')
	print('\nMarch - 03')
	print('0304\t0306\t0317\t0320\t0324\t0325')
	print('\nApril - 04')
	print('0401\t0410\t0414_S\t0414_C\t0421\t0424\n')


def main():
	print('Program selection menu:')
	while True:
		print('\n\nWhich file do you want to open?')
		print('\nInput q to exit   |   help to get help')
		inputStr = input('selection: ')

# functions of the menu
		if (inputStr == 'q'):
			print('\nProgram is shutting down...')
			break
		elif (inputStr == 'help'):
			helpOption()
		elif (inputStr == 'ls' or inputStr == 'dir'):
			ls()
# Actual file access
		#January
		elif (inputStr == '0123_1'):
			src.file0123_1.func0123_1()
		elif (inputStr == '0123_2'):
			src.file0123_2.func0123_2()
		elif (inputStr == '0128'):
			src.file0128.func0128()
		elif (inputStr == '0130t'):
			src.file0130t.func0130t()
		#February
		elif( inputStr == '0205'):
			src.file0205.func0205()
		elif (inputStr == '0206'):
			src.file0206.func0206()
		elif (inputStr == '0211'):
			src.file0211.func0211()
		elif (inputStr == '0213'):
			src.file0213.func0213()
		elif (inputStr == '0220'):
			src.file0220.func0220()
		elif (inputStr == '0225'):
			src.file0225.func0225()
		elif (inputStr == '0227_1'):
			src.file0227_1.func0227_1()
		# March
		elif(inputStr == '0304'):
			src.file0304.func0304()
		elif (inputStr == '0306'):
			src.file0306.func0306()
		elif (inputStr == '0317'):
			src.file0317.func0317()
		elif (inputStr == '0320'):
			src.file0320.func0320()
		elif (inputStr == '0324'):
			src.file0324.func0324()
		elif (inputStr == '0325'):
			src.file0325.func0325()
		# April
		elif (inputStr == '0401'):
			src.file0401.func0401()
		elif (inputStr == '0410'):
			src.file0410.func0410()
		elif (inputStr == '0414_S'):
			src.file0414_1classStudent.func0414()
		elif (inputStr == '0414_C'):
			print('Program produces no output.\nPlease check source code for reference.\n')
		elif (inputStr == '0421'):
			src.file0421.func0421()
		elif (inputStr == '0424'):
			src.file0424.func0424()
main()
