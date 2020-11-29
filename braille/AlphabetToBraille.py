from .SymbolsBraille import DictLetters, DictNumbers

class AlphabetToBraille:

	def __init__(self):
		self.brailleSymbols = DictLetters()
		self.brailleNumbers = DictNumbers()


	def convert(self, sen):
		s = ''
		if (sen == ''):
			return ''

		lines = sen.split('\n')
		for line in lines:
			words = line.split()
			for word in words:
				s += self.brailleWord(word) + ' '
			s += '\n'

		return s

	def isNumber(self, n):
		return n.isdigit()
	        

	def brailleWord(self, letters):
		word = ''
		currentLetter = ''

		if (self.isNumber(letters)):
			return self.brailleNumbers['numSymb'] + self.brailleNums(letters)

		for letter in letters:
			currentLetter = self.brailleSymbols[letter] if letter in self.brailleSymbols else ''
			word += currentLetter

		return word

	def brailleNums(self, letters):
		word = ''
		currentLetter = ''
		for letter in letters:
			currentLetter = self.brailleNumbers[letter]
			word += currentLetter

		return word