class MiClase:
    def __init__(self):
        self.publico = "Esto es público"
        self._privado = "Esto es privado"
        self.__privado_mangle = "Esto es privado con name mangling"

objeto = MiClase()

print(objeto.publico)  # Acceso público
print(objeto._privado)  # Acceso "privado", pero no se recomienda
# print(objeto.__privado_mangle)  # Esto generará un error, ya que el nombre se ha modificado

print(objeto._MiClase__privado_mangle)  # Acceso utilizando name mangling