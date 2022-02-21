#Ingresamos tarjetas
tarjeta = list(input("Ingresar Tarjeta: ").strip())
#Separamos el primer digito de derecha a izquierda
numero = tarjeta.pop()
#Reversamos la cadena para poder obtener las pocisiones de derecha a izquierda
tarjeta.reverse()
#recorremos la cadena
digitos = []
for index, digito in enumerate(tarjeta):
    if index % 2 == 0:
        doble = int(digito) * 2
        if doble > 9:
            doble = doble - 9 
        digitos.append(doble)
    else:
        digitos.append(int(digito))

total = int(numero) + sum(digitos)
if total % 10 == 0:
    print("Valida")
else:
    print("Invalida")



