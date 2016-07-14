
class Prestamo():
	"""
	Autor: Erika Narv�ez
	Nombre de funci�n: valor_total
	Entrada: valor del prestamo, y tiempo de plazo
	Salida: capital total a devolver al banco
	Descripci�n: Funci�n que realiza los respectivos calculos para obtener el valor a pagar del prestamo pedido en un tiempo plazo.
	"""
	def valor_total(self,prestamo,tiempo):
		if(prestamo < 5000):
			tiempo = 3
			comision=(prestamo *2)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1)/100)*tiempo)
			print ("Capital prestado:",prestamo)
			print("%de comision:", comision)
			print ("%de interes:", interes)
			return float(capital_total+interes)
			
		if((prestamo>= 5000) and (prestamo <= 9999.99)):
			tiempo=6
			comision=(prestamo*3)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.25)/100)*tiempo)
			print("-----------------------------------");
			print ("Capital prestado:",prestamo)
			print("%de comision:", comision)
			print ("%de interes:", interes)
			return float(capital_total+interes)

		if(prestamo >= 10000 and prestamo <= 20000):
			tiempo= 12
			comision=(prestamo*4)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.5)/100)*tiempo)
			print("-----------------------------------");
			print ("Capital prestado:",prestamo)
			print("%de comision:", comision)
			print ("%de interes:", interes)
			return float(capital_total+interes)

		if(prestamo > 20000):
			tiempo = 6
			print("-----------------------------------");
			print ("Capital prestado:",prestamo)
			print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
			return None