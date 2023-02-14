import operadores as op

print("indica el primer numero:")
numero1 = int(input())
print("indica el segundo numero:")
numero2 = int(input())

while True:
    print("selecciona el operador (+,-,*,/)")
    operacion = input()

    if operacion == "+":
        result_suma = op.suma(numero1, numero2)
        print(numero1, operacion, numero2, "=", result_suma)
        break
    elif operacion == "-":
        result_resta = op.resta(numero1, numero2)
        print(numero1, operacion, numero2, "=", result_resta)
        break
    elif operacion == "*":
        result_multiplica = op.multiplica(numero1, numero2)
        print(numero1, operacion, numero2, "=", result_multiplica)
        break
    elif operacion == "/":
        result_divide = op.divide(numero1, numero2)
        print(numero1, operacion, numero2, "=", result_divide)
        break
    else:
        print("Operador no válido. Por favor, seleccione un operador válido.")




