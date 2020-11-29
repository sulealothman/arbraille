class BrailleFile:

	def read(self, filePath=""):
		path = filePath if(filePath.strip() != "") else input("Enter file path for translate : ")
		path = path if(path.find('\\')) else path.replace('\\', '\\\\')
		with open(path, "r", encoding='utf-8') as f: content = f.read()
		return content

	def write(self, content, filePath=""):
		path = filePath if(filePath.strip() != "") else input("Enter output file path for translate : ")
		path = path if(path.find('\\')) else path.replace('\\', '\\\\')
		with open(path, 'w', encoding='utf-8') as w: w.write(content)
		return content