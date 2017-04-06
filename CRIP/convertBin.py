class convertBin:

	def __init__(self):
		self.__alfabeto = self.__geraAlfabeto()

	def __geraAlfabeto(self):
		alfabeto = dict()
		for i in range(0, 26):
			tmp = bin(i)[2:].zfill(5)
			alfabeto[tmp] = chr(65 + i)
		return alfabeto

	def StrintToBin(self, string):
		binario = ''
		string = string.upper()
		string = string.replace(' ','')
		alfa = {v: k for k,v in self.__alfabeto.items()}
		for x in string:
			binario += alfa.get(x)
		return binario

	def BinToString(self, string):
		texto = ''
		for x in range(0,len(string)//5):
			texto += self.__alfabeto.get(string[x*5:x*5+5])
		return texto

#Para fins de Texte
if __name__ == '__main__':
	B = convertBin()
	M = B.StrintToBin(input())
	print(M)
	print(B.BinToString(M))