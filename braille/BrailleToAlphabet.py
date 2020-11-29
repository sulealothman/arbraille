from .SymbolsBraille import DictLetters, DictNumbers

class BrailleToAlphabet:

	def __init__(self):
		self.brailleSymbols = DictLetters()
		self.brailleNumbers = DictNumbers()


	def convert(self, sen):
		s = ''
		if (sen == ''):
			return ''

		lines = sen.split('\n')
		for line in lines:
			words = line.split();
			for word in words:
				s += self.alphaWord(word) + ' '
			s += '\n'
		return s

	def getKeyAsString(self, dic, value):
	    for name in dic:
	        if dic[name] == value:
	            return name
			
	def alphaWord(self, letters):
		word = ''
		currentLetter = ''
		if (self.brailleNumbers['numSymb'] in letters and letters != ' '):
			letters = letters[1:]
			return self.alphaNums(letters)

		for letter in letters:
			currentLetter = self.getKeyAsString(self.brailleSymbols, letter)
			currentLetter = '' if (currentLetter == None) else currentLetter
			word += currentLetter

		return word


	def alphaNums(self, letters):
		word = ''
		currentLetter = ''
		for letter in letters:
			currentLetter = self.getKeyAsString(self.brailleNumbers, letter)
			word += currentLetter

		return word