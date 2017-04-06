from convertBin import *

class Bacon(convertBin):

	def cifra(self, string):
		M = self.StrintToBin(string)
		M = M.replace('0','A')
		M = M.replace('1','B')
		return M

	def decifra(self, string):
		string = string.replace('A','0')
		string = string.replace('B','1')
		M = self.BinToString(string)
		return M


print("Bacon Class")
C = Bacon()
texto = "Erico"
codigo = C.cifra(texto)
print("Mensagem: %s"%texto)
print("Mensagem Cifrada: %s"%codigo)
print("Mensagem Decifrada: %s"%C.decifra(codigo))