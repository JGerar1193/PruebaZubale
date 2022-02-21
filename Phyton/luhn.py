def digitSum(myString):
    longitud = len(myString)
    osum = 0
    esum = 0

    if (longitud ==0):
        return 0
    else:
        if(longitud % 2 == 0):
            last = int(myString[-1])
            esum += last
            return esum + digitSum(myString[:-1])
        else:
            last = int(myString[-1])
            last = 2 * last
            part_sum = last // 10 + last % 10
            osum += part_sum

            return osum + digitSum(myString[:-1])
def luhns():
    myString = input('Ingrese Numero de Tarjeta: ')
    total = digitSum(myString)

    if (total % 10 == 0):
        print('Tarjeta Valida')
    else:
        print('Tarjeta Invalida')

def main():
    luhns()

main()
