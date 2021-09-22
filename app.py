from models.transform import Transform
from models.modelsCargaMasiva import CargaMasiva
###
data = Transform(directorio="models/files", nombreArchivo="dummy.xlsx", hoja="pregunta")
lista_opcion = data.generate_list_option()
###
cargas = CargaMasiva(databaseURL="")
cargas.carga_pregunta_bacth(lista_opcion)
