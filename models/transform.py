import pandas as pd
class Transform():
    directorio = ""
    nombreArchivo = ""
    dfDummy = pd.DataFrame()
    def __init__(self, directorio, nombreArchivo, hoja):
        self.directorio = directorio
        self.nombreArchivo = nombreArchivo
        if self.nombreArchivo != "" and self.directorio != "" and hoja != "":
            self.dfDummy = pd.read_excel(self.directorio + "/" + self.nombreArchivo, sheet_name=hoja)
        else:
            self.dfDummy = pd.read_excel(self.directorio + "/" + self.nombreArchivo)
            
    def generate_list_question(self):
        lista1 = list(tuple([
            self.dfDummy['texto_pregunta'][i],
            self.dfDummy['materia_id'][i],
            self.dfDummy['examen_id'][i]])
                        for i in range(len(self.dfDummy)))
        return lista1
    
    def generate_list_option(self):
        lista1 = list(tuple([
            self.dfDummy['texto_pregunta_1'][i],
            bool(self.dfDummy['Opcion_1'][i]),
            self.dfDummy['texto_pregunta_2'][i],
            bool(self.dfDummy['Opcion_2'][i]),
            self.dfDummy['texto_pregunta_3'][i],
            bool(self.dfDummy['Opcion_3'][i]),
            self.dfDummy['texto_pregunta_4'][i],
            bool(self.dfDummy['Opcion_4'][i]) 
            ])
                        for i in range(len(self.dfDummy)))
        return lista1