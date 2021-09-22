import pandas as pd

preguntas_mate = [
    {
        "texto_pregunta": "La expresión 2x + 3 = 7 es una",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"inecuacion",
                "es_correcta": False
            },
            {
                "texto_opcion":"desigualdad",
                "es_correcta": False
            },
            {
                "texto_opcion":"ecuación",
                "es_correcta": True
            },
            {
                "texto_opcion":"identidad",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Al resolver 3x + 2  = 4, ¿cuál es el valor x",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x = 2/3",
                "es_correcta": True
            },
            {
                "texto_opcion":"x = 3/6",
                "es_correcta": False
            },
            {
                "texto_opcion":"x = 3/2",
                "es_correcta": False
            },
            {
                "texto_opcion":"x = 6/3",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Al resolver -2x + 6 >= 16, ¿cuál es el valor de x?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x < -5",
                "es_correcta": False
            },
            {
                "texto_opcion":"x mayor o igual a 5",
                "es_correcta": False
            },
            {
                "texto_opcion":"x menor o igual a -5",
                "es_correcta": True
            },
            {
                "texto_opcion":"x > 5",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿Cuál de las siguientes funciones tienen un comportamiento creciente?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"f(x) = -3x",
                "es_correcta": False
            },
            {
                "texto_opcion":"f(x) = 3 elevado a -x",
                "es_correcta": False
            },
            {
                "texto_opcion":"3/x",
                "es_correcta": False
            },
            {
                "texto_opcion":"x al cubo",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "A cuánto equivale 45° en radianes",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"1/4 pi",
                "es_correcta": True
            },
            {
                "texto_opcion":"2/3 pi",
                "es_correcta": False
            },
            {
                "texto_opcion":"3/4 pi",
                "es_correcta": False
            },
            {
                "texto_opcion":"4/3 pi",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Selecciona la función que tiene un desplazamiento de fase de pi unidades a la derecha",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"f(x) = sen(pi x)",
                "es_correcta": False
            },
            {
                "texto_opcion":"f(x) = sen( x + pi)",
                "es_correcta": False
            },
            {
                "texto_opcion":"f(x) = sen(x - pi)",
                "es_correcta": True
            },
            {
                "texto_opcion":"f(x) = pi sen(x)",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Encuentra las coordenadas del punto medio entre los puntos P(0,2) y Q(4,6)",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"(2,3)",
                "es_correcta": False
            },
            {
                "texto_opcion":"(2,4)",
                "es_correcta": True
            },
            {
                "texto_opcion":"(1,4)",
                "es_correcta": False
            },
            {
                "texto_opcion":"(1,5)",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Un triángulo está conformado por los vértices P(-7,1), Q(9,3) y R(3,5), ¿cuál es la ecuación de la mediana que pasa por el vértice P?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x -8y + 15 = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"3x + 13y - 34 = 0",
                "es_correcta": True
            },
            {
                "texto_opcion":"3x - y + 22 = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"2x -5y + 19 = 0",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "La ecuación de la parábola cuyo eje focal es el eje y, con el parámetro p= -5 y vértice en el origen es",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x^2 - 20x = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"y^2 - 20x = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"y^2 + 20x = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"x^2 + 20y = 0",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "Determina la expresión algebraica que cumplen las coordenadas de los puntos P(x,y), si la suma de sus distancias a los puntos F1(0,-2) y F2(0,2) es igual a 8.",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"3x^2 + 4y^2 -48 = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"4x^2 + 3y^2 - 48 = 0",
                "es_correcta": True
            },
            {
                "texto_opcion":"16x^2 + 12y^2 - 19 = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"12x^2 + 16y^2- 19 = 0",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "La ecuación de la hipérbola centrada en el orgien con lado recto igual a 10 y vértice en V(0,-9) es",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"9x^2-5y^2 = 405",
                "es_correcta": False
            },
            {
                "texto_opcion":"5y^2-9x^2 = 405",
                "es_correcta": True
            },
            {
                "texto_opcion":"9x^2 - 10y^2 = 90",
                "es_correcta": False
            },
            {
                "texto_opcion":"10x^2 - 9y^2 = 90",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "A partir de la siguiente ecuación de segundo grado determina el criterio utilizado para representar una elipse",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"C^2 - 4AB < 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"B^2 - 4AC > 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"C^2 - 4AB > 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"B^2 - 4AC < 0",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "La función f(x) = |x| es derivable en todo punto de su dominio, excepto, en",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"-2",
                "es_correcta": False
            },
            {
                "texto_opcion":"-1",
                "es_correcta": False
            },
            {
                "texto_opcion":"0",
                "es_correcta": True
            },
            {
                "texto_opcion":"2",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "La pendiente de la tangente a la curva f(x)=e^3x en el punto P(0,1)  es igual a",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"0",
                "es_correcta": False
            },
            {
                "texto_opcion":"1",
                "es_correcta": False
            },
            {
                "texto_opcion":"2",
                "es_correcta": False
            },
            {
                "texto_opcion":"3",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "¿A cuántos grados equivalen 11/18 pi radianes",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"220°",
                "es_correcta": False
            },
            {
                "texto_opcion":"110°",
                "es_correcta": True
            },
            {
                "texto_opcion":"169°",
                "es_correcta": False
            },
            {
                "texto_opcion":"198°",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿A cuántos grados equivalen 11/18 pi radianes?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"220°",
                "es_correcta": False
            },
            {
                "texto_opcion":"110°",
                "es_correcta": True
            },
            {
                "texto_opcion":"169°",
                "es_correcta": False
            },
            {
                "texto_opcion":"198°",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿Cuál es la ecuación de la asíntota vertical de la siguiente función: f(x) = 2log(x-3)?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x = 3",
                "es_correcta": True
            },
            {
                "texto_opcion":"y = -3",
                "es_correcta": False
            },
            {
                "texto_opcion":"x = -3",
                "es_correcta": False
            },
            {
                "texto_opcion":"y = 3",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Encuentra las coordenadas del punto S que divide por la mitad al segmento conformado por los puntos P(-1,2) y Q(-2,5)",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"S(-0.5,3.5)",
                "es_correcta": False
            },
            {
                "texto_opcion":"S(-1.5,2.5)",
                "es_correcta": False
            },
            {
                "texto_opcion":"S(-2.5,3.5)",
                "es_correcta": False
            },
            {
                "texto_opcion":"S(-1.5, 3.5)",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "La pendiente de la recta 3x + 6y - 1 = 0",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"-3",
                "es_correcta": False
            },
            {
                "texto_opcion":"-1/2",
                "es_correcta": True
            },
            {
                "texto_opcion":"1/2",
                "es_correcta": False
            },
            {
                "texto_opcion":"3",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Determina la ecuación de la parábola con directriz x +3 = 0, vértice en el origen y eje focal que coincide con el eje x.",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"-3",
                "es_correcta": False
            },
            {
                "texto_opcion":"-1/2",
                "es_correcta": True
            },
            {
                "texto_opcion":"1/2",
                "es_correcta": False
            },
            {
                "texto_opcion":"3",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Dada la ecuación general de segundo grado con dos variables Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, si B = 0, se tiene que",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"la cónica pasa por el origen del marco de referencia",
                "es_correcta": False
            },
            {
                "texto_opcion":"los ejes de simetría de la cónica son paralelos a los ejes coordenados",
                "es_correcta": True
            },
            {
                "texto_opcion":"los ejes de simetría de la cónica son perpendiculares a los ejes coordenados",
                "es_correcta": False
            },
            {
                "texto_opcion":"la cónica está centrada en el origen del marco de referencia",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Un estudiante debe obtener un promedio mínimo de 8 y calificaciones no menores a 7 en cada uno de los cuatro parciales. Si tiene las siguientes calificaciones en los primeros 3 parciales: 7.2, 8.5 y 7.9, ¿cuál es la mínima calificación que deberá obtener en el último parcial para aprobar el curso?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"8.1",
                "es_correcta": False
            },
            {
                "texto_opcion":"8.2",
                "es_correcta": False
            },
            {
                "texto_opcion":"8.4",
                "es_correcta": True
            },
            {
                "texto_opcion":"8.9",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿Cuántos conejos C y gallinas G hay en un corral si en su conjunto hacen un total de 61 cabezas y 196 patas?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"C = 47, G = 14",
                "es_correcta": False
            },
            {
                "texto_opcion":"C = 40, G = 21",
                "es_correcta": False
            },
            {
                "texto_opcion":"C = 37, G = 24",
                "es_correcta": True
            },
            {
                "texto_opcion":"C = 35, G = 26",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿Cuál es valor de y en la siguiente ecuación y = 5x^4 + 3x, considera x = 1?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"23",
                "es_correcta": False
            },
            {
                "texto_opcion":"9",
                "es_correcta": False
            },
            {
                "texto_opcion":"12",
                "es_correcta": False
            },
            {
                "texto_opcion":"8",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "Si 2 pi radianes equivalen a 360°, ¿a cuánto equivale un ángulo de 7/8 pi radianes?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"315°",
                "es_correcta": False
            },
            {
                "texto_opcion":"145°30'",
                "es_correcta": False
            },
            {
                "texto_opcion":"270°",
                "es_correcta": False
            },
            {
                "texto_opcion":"157°30'",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "El dominio de la función f(x) = log(x - 1) es",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x menor o igual a 1",
                "es_correcta": False
            },
            {
                "texto_opcion":"x < 1",
                "es_correcta": False
            },
            {
                "texto_opcion":"x > 1",
                "es_correcta": True
            },
            {
                "texto_opcion":"x mayor o igual a 1",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Calcula la pendiente de la recta cuya función es 2y - 4x + 3 = 0",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"-2",
                "es_correcta": False
            },
            {
                "texto_opcion":"-1/2",
                "es_correcta": True
            },
            {
                "texto_opcion":"2/3",
                "es_correcta": False
            },
            {
                "texto_opcion":"2",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿Cuál es la ecuación de la recta que pasa por el punto P(5,2) y es paralela a la recta que pasa por los puntos Q(2,-6) y R(-1,3)",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"y = -2x -9",
                "es_correcta": False
            },
            {
                "texto_opcion":"y = -4x + 3",
                "es_correcta": False
            },
            {
                "texto_opcion":"y = -5x - 11",
                "es_correcta": False
            },
            {
                "texto_opcion":"y = -3x + 17",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "¿Cuál es la ecuación de la circunferencia que tiene centro en el origen y radio igual a 4?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x^2 + y^2 + 16 = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"x^2 + y^2 - 16 = 0",
                "es_correcta": True
            },
            {
                "texto_opcion":"x^2 + y^2 - 4 = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"x^2 + y^2 + 4 = 0",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Determina el centro y el radio de la siguiente circunferencia: (x+4)^2 + (y-6)^2 = 49",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"C(-4,6), r = 7",
                "es_correcta": True
            },
            {
                "texto_opcion":"C(4,-6), r = 7",
                "es_correcta": False
            },
            {
                "texto_opcion":"C(-4,6), r = 49",
                "es_correcta": False
            },
            {
                "texto_opcion":"C(4,-6), r = 49",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "La expresión x = 4y^2 + 8y + 2",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"circunferencia",
                "es_correcta": False
            },
            {
                "texto_opcion":"hipérbola",
                "es_correcta": False
            },
            {
                "texto_opcion":"elipse",
                "es_correcta": False
            },
            {
                "texto_opcion":"parábola",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "Un estacionmaiento para 1,000 automóviles. Un día hubo 200 autos compactos y algunos estándar, ocupando 3/4 partes de su capacidad, ¿cuántos autos de tamaño estándar había en el estacionamiento",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"500",
                "es_correcta": False
            },
            {
                "texto_opcion":"550",
                "es_correcta": True
            },
            {
                "texto_opcion":"600",
                "es_correcta": False
            },
            {
                "texto_opcion":"650",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿Cuál es la solución al resolver la siguiente desigualdad: 5 + x > 8?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x > 3",
                "es_correcta": True
            },
            {
                "texto_opcion":"x > 2",
                "es_correcta": False
            },
            {
                "texto_opcion":"x > 8",
                "es_correcta": False
            },
            {
                "texto_opcion":"x > 13",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "¿A cuántos grados equivalen 11/18 pi radianes?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"220°",
                "es_correcta": False
            },
            {
                "texto_opcion":"110°",
                "es_correcta": True
            },
            {
                "texto_opcion":"169°",
                "es_correcta": False
            },
            {
                "texto_opcion":"198°",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Un objeto es lanzado describiendo la parábola (x-4)^2 = 12(y-3), ¿cuáles son las coordenadas del vértice V y el foco F?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"V(-4,-3), F(-4,-6)",
                "es_correcta": False
            },
            {
                "texto_opcion":"V(3,4), F(6,4)",
                "es_correcta": False
            },
            {
                "texto_opcion":"V(4,3), F(4,6)",
                "es_correcta": True
            },
            {
                "texto_opcion":"V(-3,-4), F(-6,-4)",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Al transaldar la circunferencia x^2 + y^2  - 36 = 0 al centro C(-2,4), ¿cuál sería su ecuación?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"(x-4)^2 + (y+16)^2 = 36",
                "es_correcta": False
            },
            {
                "texto_opcion":"(x+4)^2 + (y-16)^2 = 36",
                "es_correcta": False
            },
            {
                "texto_opcion":"(x+2)^2 + (y-4)^2 = 36",
                "es_correcta": True
            },
            {
                "texto_opcion":"(x-2)^2 + (y+4)^2 = 36",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Los valores de 0 y -2 son las raíces o soluciones de la ecuación",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"x(x-2) = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"(x+2)(x-2) = 0",
                "es_correcta": False
            },
            {
                "texto_opcion":"x(x+2) = 0",
                "es_correcta": True
            },
            {
                "texto_opcion":"x^2 - 4 = 0",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "Si S = {1,2} y Q = {2,3,4}, ¿cuál es el rango de la función f: S -> Q definida por f(x) = x + 1?",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"{2,3}",
                "es_correcta": True
            },
            {
                "texto_opcion":"{2,4}",
                "es_correcta": False
            },
            {
                "texto_opcion":"{1,3}",
                "es_correcta": False
            },
            {
                "texto_opcion":"{2,3,4}",
                "es_correcta": False
            }
        ]
    },
    {
        "texto_pregunta": "La distancia entre los puntos P(2,5) y Q(4,-1) es",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"raíz de 12",
                "es_correcta": False
            },
            {
                "texto_opcion":"raíz de 20",
                "es_correcta": False
            },
            {
                "texto_opcion":"raíz de 32",
                "es_correcta": False
            },
            {
                "texto_opcion":"raíz de 40",
                "es_correcta": True
            }
        ]
    },
    {
        "texto_pregunta": "El foco de la parábola y^2 - 8x = 0 es el punto",
        "materia_id": 1,
        "opciones": [
            {
                "texto_opcion":"(8,0)",
                "es_correcta": False
            },
            {
                "texto_opcion":"(2,0)",
                "es_correcta": False
            },
            {
                "texto_opcion":"(-2,0)",
                "es_correcta": False
            },
            {
                "texto_opcion":"(-8,0)",
                "es_correcta": True
            }
        ]
    },
]
arreglo_pregunta = []; arreglo_materia = []
arreglo_opcion_txt= []; arreglo_correcta =[]#
####
text0_opcion =[];opcion0_correcta=[]
text1_opcion =[];opcion1_correcta=[]
text2_opcion =[];opcion2_correcta=[]
text3_opcion =[];opcion3_correcta=[]
for i in range(len(preguntas_mate)):
    ##########
    arreglo_pregunta.append(preguntas_mate[i]['texto_pregunta'])
    arreglo_materia.append(preguntas_mate[i]['materia_id'])
    ######
    for t in range(len(preguntas_mate[i]['opciones'])):
        if t ==0:
            text0_opcion.append(preguntas_mate[i]['opciones'][t]['texto_opcion'])
            opcion0_correcta.append(preguntas_mate[i]['opciones'][t]['es_correcta'])
        if t ==1:
            text1_opcion.append(preguntas_mate[i]['opciones'][t]['texto_opcion'])
            opcion1_correcta.append(preguntas_mate[i]['opciones'][t]['es_correcta'])
        if t ==2:
            text2_opcion.append(preguntas_mate[i]['opciones'][t]['texto_opcion'])
            opcion2_correcta.append(preguntas_mate[i]['opciones'][t]['es_correcta'])
        if t ==3:
            text3_opcion.append(preguntas_mate[i]['opciones'][t]['texto_opcion'])
            opcion3_correcta.append(preguntas_mate[i]['opciones'][t]['es_correcta'])
###
df = pd.DataFrame()
df['texto_pregunta'] = arreglo_pregunta
df['materia_id'] = arreglo_materia
##
df['texto_pregunta 1'] = text0_opcion
df['Opcion 1'] = opcion0_correcta
###
df['texto_pregunta 2'] = text1_opcion
df['Opcion 2'] = opcion1_correcta
####
df['texto_pregunta 3'] = text2_opcion
df['Opcion 3'] = opcion2_correcta
####
df['texto_pregunta 4'] = text3_opcion
df['Opcion 4'] = opcion3_correcta
print(df)
df.to_excel("preguntas.xlsx")