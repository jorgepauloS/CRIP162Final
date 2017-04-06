#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
from numpy import  *
from convertBin import *

class Reticulados(convertBin):

	def geraMatrix(self, N):
		tmp = []
		for x in range(N):
			linha = []
			for y in range(N):
				linha.append(random.randint(0, 1000))
			tmp.append(linha)
		if det(Matrix(tmp)) != 0:
			return tmp
		else:
			geraMatrix(N)

	def Codifica(self, mesg):
		mesg = '1'+mesg
		M = self.geraMatrix(len(mesg))
		codigo = [int(x) for x in mesg]

		l = [0]*len(M[0])	
		for i in range(len(M)):
			for x in range(len(M[i])):
				if codigo[i] == 1:
					l[x] = l[x] + M[i][x]

		return l, M

	def DeCodifica(self, codigo, M):
		me = []
		decode = squeeze(asarray(Matrix(codigo).T*Matrix(M).inv()))
		for x in decode:
			me.append(int(x))

		me.pop(0)
		return ''.join(map(str,me))

	def cifraCodifica(self, string):
		codigoEncriptdo , matriz = self.Codifica(self.StrintToBin(string))
		return codigoEncriptdo , matriz

	def cifraDeCodifica(self, vet, mat):
		return  self.BinToString(self.DeCodifica(vet , mat))



r = Reticulados()

texto_puro = input("Digite um texto: ")
print("\nMensagen: %s "%texto_puro)

codigo, matriz = r.cifraCodifica(texto_puro)
codigoDecriptado = r.cifraDeCodifica(codigo , matriz)

print("\nMensagen Codificada: %s "%' '.join(list(map(str, codigo))))

print("\nMensagen Decodificada: %s "%codigoDecriptado)