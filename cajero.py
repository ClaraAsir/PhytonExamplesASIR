#! usr/bin/env phython
# -*- encoding:utf- 8 -*-


class Cajero:
	
	saldo=0.0
	
	
	def __init__(self,saldoinicial):
		self.saldo = saldoinicial
		
		
	def ingreso_efectivo(self,cantingresar):
		self.saldo+=cantingresar
		print("Se ingresó %.2f €" % cantingresar)
		print("Saldo actual:  %.2f" % self.saldo)
		
		
	def retirada_efectivo(self,cantretirar):
		if self.saldo > cantretirar:
			self.saldo-=cantretirar
			
			print("\n\n\nSe retiraron: %.2f €" % cantretirar)
			print("Saldo actual:  %.2f €" % self.saldo)
		else:
			print("No hay saldo suficiente")
		

objcajero=Cajero(521)
objcajero.ingreso_efectivo(21)
objcajero.retirada_efectivo(32)
