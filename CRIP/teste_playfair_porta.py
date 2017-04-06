# -*- coding:utf-8 -*-

from playfair import Playfair

txt_in = input('Texto a ser cifrado: ')
password = input('Senha: ')
 
cifra = Playfair()
cifrado = cifra.encrypt(txt_in, password)
print(cifrado)
texto_inNovo = cifra.decrypt(cifrado, password)
decifrado = cifra.decrypt(cifrado, password)
if decifrado[-1] =='w':
	decifrado = decifrado[0:len(decifrado)-1]

print(decifrado)

""" Opcional para gera arquivo de saida"""

arq = open('cifrado.txt','w')
arq.write(texto_inNovo)
arq.write("senha: "+password)
arq.write('\nTexto Cifrado: '+cifrado)
arq.write('\nTexto decryptado: '+texto_inNovo)

arq.close()