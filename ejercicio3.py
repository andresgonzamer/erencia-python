# declaramos la clase persona
class Calculadora:
    # declaramos el metodo __init__
    def __init__(self):
        self.valor1=int(input("Ingrese el valor 1 : "))
        self.valor2=int(input("ingrese el valor 2: ")) 
      
    def Sumar(self):
      suma=self.valor1+self.valor2
      print(suma)
 
    def Restar(self):
      resta=self.valor1-self.valor2
      print(resta)

    def Multiplicar(self):
      mult=self.valor1*self.valor2
      print(mult)
       
    def Vidir(self):
      div=self.valor1+self.valor2
      print(div)
      
suma1=Calculadora()
suma1.Sumar()
suma1.Restar()
suma1.Multiplicar()
suma1.Vidir()