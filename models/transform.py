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
        lista = list(tuple([
            int(self.dfDummy['pregunta_id'][i]),
            str(self.dfDummy['texto_pregunta'][i]),
            int(self.dfDummy['materia_id'][i]),
            int(self.dfDummy['examen_id'][i])])
                        for i in range(len(self.dfDummy)))
        return lista
    
    def generate_list_option_1(self):
        lista = list(tuple([
            int(self.dfDummy['pregunta_id'][i]),
            str(self.dfDummy['texto_pregunta_1'][i]),
            bool(self.dfDummy['Opcion_1'][i]) 
            ])
                        for i in range(len(self.dfDummy)))
        return lista
    
    def generate_list_option_2(self):
        lista = list(tuple([
            int(self.dfDummy['pregunta_id'][i]),
            str(self.dfDummy['texto_pregunta_2'][i]),
            bool(self.dfDummy['Opcion_2'][i]) 
            ])
                        for i in range(len(self.dfDummy)))
        return lista
    
    def generate_list_option_3(self):
        lista = list(tuple([
            int(self.dfDummy['pregunta_id'][i]),
            str(self.dfDummy['texto_pregunta_3'][i]),
            bool(self.dfDummy['Opcion_3'][i]) 
            ])
                        for i in range(len(self.dfDummy)))
        return lista   
     
    def generate_list_option_4(self):
        lista = list(tuple([
            int(self.dfDummy['pregunta_id'][i]),
            str(self.dfDummy['texto_pregunta_4'][i]),
            bool(self.dfDummy['Opcion_4'][i]) 
            ])
                        for i in range(len(self.dfDummy)))
        return lista