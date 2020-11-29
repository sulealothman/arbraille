import sys, argparse
from .AlphabetToBraille import AlphabetToBraille
from .BrailleToAlphabet import BrailleToAlphabet
from .BrailleFile import BrailleFile

class Main:
	def __init__(self):
		self.args = self.arguments()
		self.alphaBraille = AlphabetToBraille()
		self.brailleAlpha = BrailleToAlphabet()
		self.braileFile = BrailleFile()
		self.mainLoop(self.args)
		


	def arguments(self):
		self.parser = argparse.ArgumentParser(
		description="Script name : arbraille, Ver. : 0.1, Author : SuleAlOthman",
		usage=""" Example #1 : python3 arbraille.py -t ar2br -f filename.txt -o output.txt \r\n""")
		self.parser.add_argument('-f', '--file',type=str, help='Input Text file for Translating')
		self.parser.add_argument('-o', '--output',type=str, help='Output Text file for Translating')
		self.parser.add_argument('-t', '--translating',type=str, help='translating type : ar2br or br2ar')
		return self.parser.parse_args()
		
	
	def mainLoop(self, args):
		if(args.file == None and args.output == None and args.translating == None):
			self.Options()
		elif(args.file == None or args.output == None or args.translating == None):
			print("Abort, please insert all arguments if you want usage a script command line")
			self.quit()
		else:
			try:
				inputFile = self.braileFile.read(args.file.strip())
				print(inputFile)
				convert = self.translate(inputFile, args.translating.strip())
				print(convert)
				if(convert != False):
					output = self.braileFile.write(convert, args.output)
				print("Successfully Convert.")
			except:
				print("Err.")
		

	def showOptions(self):
		print("1 => ar2br (arabic to braille")
		print("2 => br2ar (braille to arabic")
		print("3 => Show Options")
		print("4 => for exit.")


	def Options(self):
		self.showOptions()
		while True:
			try:
				selectType = int(input("Select translate type : ").strip())
				self.choose(selectType)
			except:
				print("Please don't enter any character,\nPlease enter your option choose \n  ")


	def choose(self, selectType):
		if(selectType == 1):
			inputX = input("Enter your Text :\n")
			content = self.alphaBraille.convert(inputX)
			print(content)
		elif(selectType == 2):
			inputX = input("Enter your Text :\n")
			content = self.brailleAlpha.convert(inputX)
			print(content)
		elif(selectType == 3):
			self.showOptions()
		elif(selectType == 4):
			self.quit()
		else:
			print("Please enter your option choose \n ")

	def translate(self, txt, trans='ar2br'):
		if trans == 'ar2br':
			return self.alphaBraille.convert(txt)
		elif trans == 'br2ar':
			return self.brailleAlpha.convert(txt)
		else:
			return False

	def quit(self):
		sys.exit(self)


