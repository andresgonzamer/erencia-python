# declaramos la clase persona
class Alumno:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre del alumno: ")
        super().__init__()
        self.nota=float(input("Ingrese la nota del alumno: "))
 
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre del Alumno: ",self.nombre)
        print("Nota del Alumno: ",self.nota)
 
 
    # declaramos el metodo mostrar
        def mostrar(self):
          super().mostrar()
        print("Nota: ",self.nota)
 
 
    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no

    def pagar_impuestos(self):
        if self.nota >=3 :
          print("aprobo")
        else:
            print("no aprobo")
 
# bloque principal
Alumno1=Alumno()
Alumno1.mostrar()
Alumno1.pagar_impuestos()