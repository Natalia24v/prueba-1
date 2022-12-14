# Tarea crear tres objectos más, utilizando los métodos getter and setter
# para modificar, y mostrar los cambios con el método mostrar detalles
class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property
    def nombre(self):
        print('Se esta utilizando el Método getter')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Se esta utilizando el metodo setter')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


# objeto numero uno de la lista
persona1 = Persona2('Mora', 'Brun', 33)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
persona1.nombre = 'Moira'
persona1.apellido = 'Brown'
persona1.edad = 34
print(persona1.mostrar_detalles())

# objeto numero dos de la lista
persona2 = Persona2('Lushi', 'Wes', 24)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
persona2.nombre = 'Lucy'
persona2.apellido = 'West'
persona2.edad = 25
print(persona2.mostrar_detalles())

# objeto numero tres de la lista
persona3 = Persona2('Hard', 'Sim', 26)
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
persona3.nombre = 'Harden'
persona3.apellido = 'Simms'
persona3.edad = 27
print(persona3.mostrar_detalles())
