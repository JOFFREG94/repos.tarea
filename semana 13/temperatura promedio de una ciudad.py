#Iteración de arreglos multidimensionales con bucles anidados
temperatura = [
    [#Loja
        [12, 15, 17, 18, 20, 30, 55],#Semana 1
        [12, 14, 23, 25, 28, 14, 10],#Semana 2
        [10, 15, 15, 14, 18, 17, 18],#Semana 3
        [10, 12, 14, 16, 18, 20, 22] #Semana 4
    ],
    [#Cuenca
        [10, 12, 14, 15, 28, 26, 19],#Semana 1
        [20, 25, 25, 22, 27, 32, 31],#Semana 2
        [32, 25, 24, 27, 29, 24, 25],#Semana 3
        [30, 31, 32, 33, 33, 32, 34] #Semana 4
    ],
    [#Machala
        [20, 25, 23, 24, 21, 20, 20],#Semana 1
        [10, 14, 17, 15, 14, 17, 18],#Semana 2
        [14, 15, 20, 25, 52, 24, 20],#Semana 3
        [20, 21, 21, 24, 21, 20, 22] #Semana 4
    ]
]

#Funcion para calcular la temperatura de una ciudad y semana solicitada por el usuario

def prm_temperatura(para_temperatura, ciudad, semana):
    contador_temperatua =0
    promedio_temperatura=0
    for temperatura in range(len(para_temperatura[ciudad][semana])):
        contador_temperatua+=para_temperatura[ciudad][semana][temperatura]
    promedio_temperatura=contador_temperatua/len(para_temperatura[ciudad][semana])

    return promedio_temperatura


resultado_prom=prm_temperatura(temperatura, 1,0 )
print("El promedio de temperatura es: ",resultado_prom)