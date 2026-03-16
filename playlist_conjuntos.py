canciones_Juan ={
    "La Camisa Negra", "A Dios le Pido", "Me Enamora",
    "Volverte a Ver", "Es Por Ti", "La Flaca", "Oye Como Va", 
    "Es Por Ti", "La Flaca", "Oye Como Va"
}
canciones_Maria = {
    "Shape of you", "Despacito", "Me Enamora", 
    "Volverte a Ver", "Es Por Ti", "La Flaca", 
    "Oye Como Va", "Rolling in the Deep", "Someone Like You"
}
playlist_comun = canciones_Juan.intersection(canciones_Maria) #Intersección de los conjuntos
catalogo = canciones_Juan | canciones_Maria #Unión de los conjuntos
recomendaciones = canciones_Juan - canciones_Maria #Diferencia de los conjuntos
a = (canciones_Juan, canciones_Maria) #Conjunto de conjuntos
exclusivas = canciones_Juan ^ canciones_Maria #Diferencia simétrica de los conjuntos

#otro ejemplo

algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan"
}

bases_de_datos = {
    "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan", "Jorge"
}
redes = {
    "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan", "Jorge", "Karla"
}
estudian_todas = algoritmos & bases_de_datos & redes #Intersección de los conjuntos
estudian_algoritmos = algoritmos - (bases_de_datos | redes) #Diferencia de algoritmos con la unión de bases de datos y redes
estudian_algoritmos_redes = (algoritmos & redes) - bases_de_datos #Intersección de algoritmos y redes menos la intersección de algoritmos y bases de datos
estudian_algoritmos_o_redes = algoritmos | redes #Unión de algoritmos y redes
estudian_algoritmos_no_redes = algoritmos - redes #Diferencia de algoritmos con redes

solo_algoritmos = algoritmos - bases_de_datos - redes
solo_bases = bases_de_datos - algoritmos - redes
solo_redes = redes - algoritmos - bases_de_datos

solo_una = solo_algoritmos | solo_bases | solo_redes
print(len(solo_una))
#resumen de en que materias estan cada estudiante
#resumen = {est: [m for m, c in [("Algoritmos", algoritmos),("Bases de Datos", bases_de_datos), ("Redes", redes)] if est in c] for est in (algoritmos | bases_de_datos | redes)}

reporte = {}

todos = algoritmos | redes | bases_de_datos
