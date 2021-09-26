# Notas para la API 
## Response
### *Vista Evaluaciones*
---
Archivo: *evaluaciones.json*, el cual es un arreglo de objetos que contiene:
1. **Examen ID:** Identificador del examen. Tipo de dato - **Int**
2. **Nombre Examen:** Nombre del examen. Tipo de dato - **String**
3. **Estatus:** Describe el Status de el progreso de un Examen.Tipo de dato **String**
    * Inconcluso: Lo inicio pero no lo acabo **( I )**
    * Terminado: Lo acabó **( T )**
    * Nunca: Nunca lo abrió  **( N )**
4. **Aciertos:** Puede ser un entero o puede ser nulo
5. **Numero de preguntas Contestadas:** Tipo de dato - **Int** o **null**
6. **Total de Preguntas:** Numero total de preguntas. Tipo de dato - **Int**
7. **Intentos:** Numero de intentos que se pueden hacer en un examen. Tipo de dato - **Int**

**Código Completo**

```json
{
    "evaluciones": [{
            "examen_ID": 1,
            "nombre_examen": "Examen 1",
            "status": "I",
            "aciertos": 9,
            "num_preguntas_Contestadas": 10,
            "total_Preguntas": 20,
            "intentos": 0
        },
        {
            "examen_ID": 2,
            "nombre_examen": "Examen 2",
            "status": "T",
            "aciertos": 9,
            "num_preguntas_Contestadas": 10,
            "total_Preguntas": 20,
            "intentos": 0
        },
        {
            "examen_ID": 3,
            "nombre_examen": "Examen 2",
            "status": "N",
            "aciertos": 9,
            "num_preguntas_Contestadas": 10,
            "total_Preguntas": 20,
            "intentos": 0
        }
    ]
}
```

### *Vista de Examen*
---
Archivo: *examen.json*
1. **Evaluación ID:** El cual es el ID de el examen. Tipo de dato - **Int**
2. **Examen:** El cual es un arreglo de objetos, este arrelgo de objetos contiene:
    * **Texto de la pregunta**: Texto de la pregunta en crudo. Tipo de dato - **String**
    * **Opciones:** Arreglo de opciones, el cual contiene:
        * Opcion ID: Identificador de la opción de la pregunta; Tipo de dato - **Int**
        * Contenido de la opción: Texto en crudo de la opción; Tipo de dato - **String**
    * **Opciones Correcta ID**: Identificador de la opción Correcta; Tipo de dato - **Int**
    * **Materia ID**: Identificador de la Materia; Tipo de dato - **Int**

**Código completo**

```json
{
    "evaluacion_id": 1,
    "preguntas": [{
            "texto_pregunta": "¿Quién mato a Colosio?",
            "opciones": [{
                    "opcion_id": 1,
                    "contenido_opcion": "Salinas"
                },
                {
                    "opcion_id": 2,
                    "contenido_opcion": "ONU"
                }
            ],
            "opcion_correcta_id": 1,
            "materia_id": 1
        },
        {
            "texto_pregunta": "¿En que año cayo Roma?",
            "opciones": [{
                    "opcion_id": 1,
                    "contenido_opcion": "Salinas"
                },
                {
                    "opcion_id": 2,
                    "contenido_opcion": "ONU"
                }
            ],
            "opcion_correcta_id": 1,
            "materia_id": 1
        }
    ]
}
```

## Request
### *Examen Terminado*
---
Archivo: *examen_terminado.json*
1. **Evaluacion ID:** Identificador de la evolución, tipo de dato -  **Int**
2. **Aciertos Totales:** Aciertos de la evaluación, tipo de dato - **Int**
3. **Fecha Aplicacion:** Fecha de realización del examen, tipo de dato - **Date**
4. **Puntaje Materia:** Arreglo de objetos, el cual, contiene:
    * Materia ID: Identificador de la materia
    * Puntaje: Puntaje de la evaluación

**Código Completo**

```json
{
    "evaluacion_id": 1,
    "aciertos_totales": 2,
    "fecha_aplicacion": "Date",
    "puntaje_materia": [{
            "materia_id": 1,
            "puntaje:": 3
        },
        {
            "materia_id": 2,
            "puntaje:": 4
        }
    ]
}
```

### *Mi progreso*
---
Archivo: *mi_progreso.json*
1. **Promedio General:** Promedio de las evaluaciones, tipo de dato - **Float**
2. **Historial Evaluaciones:** Arreglo de objetos, los cuales contiene:
    * Nombre Examen: Nombre de la evaluación, tipo de dato - **String**
    * Puntaje Total: Puntos obtenidos, tipo de dato - **Int**
    * Evaluación ID: Identificador de la evaluación, tipo de dato - **Int**

**Código Completo**

```json
{
    "promedio_general": 10.4,
    "historial_evaluaciones": [{
            "nombre_examen": "Evaluacion 1",
            "puntaje_total": 20,
            "evaluacion_id": 1

        },
        {
            "nombre_examen": "Evaluacion 1",
            "puntaje_total": 20,
            "evaluacion_id": 2
        }
    ]
}
```

### *Pregunta Examen*
---
Archivo: *pregunta_examen.json*
1. **Evaluación ID:** Identificador de la evaluación
2. **Opcion Seleccionada:**
3. **Pregunta ID:** Identificador de la pregunta

**Código Completo**

```json
{
    "evaluacion_id": 1,
    "opcion_seleccionada": 1,
    "pregunta_id": 1
}
```

