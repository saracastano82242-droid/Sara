import re

texto = "sara_castano82242@elpoli.edu.co"

resultado = re.findall(r"^\w+@\w+\.\w{2,3}", texto) 

if len(resultado) > 0: #validamos si se encontraron coincidencias
    print("Se encontraron coincidencias: ", (resultado))
else:
    print("No se encontraron coincidencias.") 



#print(resultado)
#print(len(resultado), resultado)#nos imprime la cantidad de coincidencias y las coincidencias encontradas

"""
match: este método busca una coincidencia al inicio de la cadena. 
Si encuentra una coincidencia, devuelve un objeto de tipo Match; de lo contrario, devuelve None.
search: este método busca una coincidencia en cualquier parte de la cadena. 
Si encuentra una coincidencia, devuelve un objeto de tipo Match; de lo contrario, devuelve None
findall: este nos devuelve una lista con todas las coincidencias encontradas
sub: este nos permite reemplazar un patrón por otro

(re.IGNORECASE) IGNORECASE para que no distinga entre mayusculas y minusculas
 ponemos "r" para que no se confunda con black es blas 


\w: coincide con cualquier carácter alfanumérico (letras, dígitos y guiones bajos)
\s: coincide con cualquier espacio en blanco (espacios, tabulaciones, saltos de línea)
\b: coincide con un límite de palabra (el inicio o el final de una palabra)
\D: coincide con cualquier carácter que no sea un dígito
\W: coincide con cualquier carácter que no sea alfanumérico
\S: coincide con cualquier carácter que no sea un espacio en blanco
\w*: coincide con cero o más caracteres alfanuméricos
\s?: coincide con cero o un espacio en blanco


la vamos a usar mucho para validar numeros o letras

"+": coincide con una o más ocurrencias del patrón anterior (por ejemplo, \w+ coincide con una o más letras o dígitos consecutivos)
"*": coincide con cero o más ocurrencias del patrón anterior (por ejemplo, \s* coincide con cero o más espacios en blanco)
"?": coincide con cero o una ocurrencia del patrón anterior (por ejemplo, \b?
\d: coincide con cualquier dígito (equivalente a [0-9]) 
\d+: coincide con una o más ocurrencias de dígitos o numeros consecutivos 
^: coincide con el inicio de la cadena
$: coincide con el final de la cadena
\.: coincide con un punto literal (el punto es un metacarácter que coincide con cualquier carácter, 
por lo que se debe escapar con una barra invertida para buscar un punto específico)
"@": para buscar el símbolo de arroba en una dirección de correo electrónico.
"+@": para buscar una o más ocurrencias del símbolo de arroba, lo que puede ser útil para validar direcciones de correo electrónico.
"*@": para buscar cero o más ocurrencias del símbolo de arroba, lo que también puede ser útil para validar direcciones de correo electrónico.
"?@": para buscar cero o una vez (por lo menos una vez)
"{n}": es un cuantificador que se utiliza para especificar el número exacto de ocurrencias de un patrón. 
Por ejemplo, \d{3} coincide con exactamente tres dígitos consecutivos.
"[n]": se utiliza para definir un conjunto de caracteres (numeros, letras).
"[a-z]": se utiliza para definir todo tipo de letras
"n+" buscara todas las letras o numeros que estamos indicandole al +
"n[m]": se utiliza para definir un rango de caracteres (numeros, letras).
Por ejemplo, [aeiou] coincide con cualquier vocal, y [0-9] coincide con cualquier dígito.
"{n,m}": es un cuantificador que se utiliza para especificar un rango de ocurrencias de un patrón. 
Por ejemplo, \d{2,4} coincide con entre dos y cuatro dígitos
"{n,}": es un cuantificador que se utiliza para especificar un número mínimo de ocurrencias de un patrón. 
Por ejemplo, \d{3,} coincide con tres o más dígitos consecutivos
"g.j" el punto puede ser cualquier caracter, entonces va a coincidir con "gaj", "g1j", "g-j", etc.
"n|n": la utilizamos para buscar una informacion
"\": para buscar caracteres especiales, como el punto, el asterisco, el signo de interrogación, etc.
"\d+\.\d": significa que antes del "\." va a buscar numeros y despues los demas numeros 
"^": para indicar que la coincidencia debe ocurrir al inicio de la cadena.
"\(.*\)": va a encontrar la apertura y el cierre de los parentesis incluyendo lo de adentro de este
"()+": buscara todo lo que este seguido de lo que ingresemos en el parentesis
"(|)": busca todo lo que conincida
"\w+": ignorara los puntos
"^\w+@\w+\.\w": significa que vamos a evaluar el texto y que deben numeros o letras, una y debe haber un @, y despues deben aver uno o mas letras 
y numeros y depues del punto letras o numeros

12/03/2026

[-\s]: este verifica los espacios 
"""