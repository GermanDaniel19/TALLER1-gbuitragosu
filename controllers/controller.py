""" from models.perro import Perro
from models.guarderia import Guarderia

# class Controlador():

#     def __init__(self) -> None:
#         pass

perro_1 = Perro("Rufo","Labrador",22,7)
perro_2 = Perro("Bingo","Pug",6,2)
perro_3 = Perro("Lassie","collie",27,5)
guarderia_1 = Guarderia("mi guarderia","calle 123 # 1 - 2",[perro_1,perro_2,perro_3])
# print (guarderia_1.retornar_perros(perro_1,perro_2,perro_3))

perros=guarderia_1.retornar_perros()
 """