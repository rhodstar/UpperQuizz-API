from models.transform import Transform
from models.modelsCargaMasiva import CargaMasiva
import os

def app():
    ###Extraction and Tratement
    data = Transform(directorio="models/files", nombreArchivo="dummy.xlsx", hoja="pregunta")
    ###Read and Extract the questions
    question_List = data.generate_list_question()
    print(len(question_List), question_List[0])
    ###Read and Extract the option 1
    option_list1 = data.generate_list_option_1()
    print(len(option_list1), option_list1[0])
    ###Read and Extract the option 2
    option_list2 = data.generate_list_option_2()
    print(len(option_list2), option_list2[0])
    ###Read and Extract the option 3
    option_list3 = data.generate_list_option_3()
    print(len(option_list3), option_list3[0])
    ###Read and Extract the option 4
    option_list4 = data.generate_list_option_4()
    print(len(option_list4), option_list4[0])
    ###Charge or Liberation
    cargas = CargaMasiva(databaseURL=os.getenv('DATABASE'))
    #cargas.delete()
    cargas.charge_question_batch(question_List)
    cargas.charge_option_batch(option_list1)
    cargas.charge_option_batch(option_list2)
    cargas.charge_option_batch(option_list3)
    cargas.charge_option_batch(option_list4)
    ###Close Conection
    cargas.close_conexion()
app()