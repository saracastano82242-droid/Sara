# Este código genera todas las permutaciones posibles de una lista dada utilizando recursividad.
def permutaciones(lista):
    if len(lista) == 0:
        return [[]]
    
    resultado = []
    for i in range(len(lista)):
        elemento = lista[i]
        sublista = lista[:i] + lista[i+1:]
        subpermutaciones = permutaciones(sublista)
        
        for subperm in subpermutaciones:
            resultado.append([elemento] + subperm)
    
    return resultado
# Ejemplo de uso
elementos = [1, 3, 5]
permutaciones_resultado = permutaciones(elementos)
print("Permutaciones de", elementos, ":")
for perm in permutaciones_resultado:
    print(perm)