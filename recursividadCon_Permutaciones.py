# Este código genera todas las permutaciones posibles de una lista dada utilizando recursividad.
def permutaciones(lista):
    #caso base: si la lista esta vacia, hay una sola permutacion: la lista vacia
    if len(lista) == 0:
        return [[]]
    
    resultado = []
    #para cada elemento en la lista, lo tomamos como el primer elemento de la permutacion y luego generamos las permutaciones de los elementos restantes
    for i in range(len(lista)):
        #elemento actual que se va a colocar al inicio de la permutacion
        elemento = lista[i]
        #sublista que contiene todos los elementos excepto el actual
        sublista = lista[:i] + lista[i+1:]
        #generamos las permutaciones de la sublista de forma recursiva
        subpermutaciones = permutaciones(sublista)
        #para cada permutacion de la sublista, agregamos el elemento actual al inicio y lo añadimos al resultado final
        for subperm in subpermutaciones:
            #agregamos el elemento actual al inicio de la permutacion de la sublista y lo añadimos al resultado final
            resultado.append([elemento] + subperm)
    
    return resultado
# Ejemplo de uso
elementos = [1, 3, 5]
permutaciones_resultado = permutaciones(elementos)
print("Permutaciones de", elementos, ":")
for perm in permutaciones_resultado:
    print(perm)