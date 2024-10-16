def validate_first_number_cpf(cpf):
    contador1 = list()
    contador2 = list()

    while True:
        for numero in cpf:
            contador1.append(numero)
        for i in range(10, 1, -1):
            contador2.append(i)
        break

    valor = 0

    for indice, numero in zip(contador1, contador2):
        indice = int(indice)
        numero = int(numero)
        valor += indice * numero
    
    return valor

def validate_last_number_cpf(cpf):
    contador1 = list()
    contador2 = list()

    while True:
        for numero in cpf:
            contador1.append(numero)
        for i in range(11, 1, -1):
            contador2.append(i)
        break

    valor = 0

    for indice, numero in zip(contador1, contador2):
        indice = int(indice)
        numero = int(numero)
        valor += indice * numero
    
    return valor

def last_digits_validate(value):
    digit = 11 - (value % 11)
    return digit

def cpf_format(cpf):
    numero = str(cpf)
    numero = numero.split('.')
    numero = ''.join(numero)
    numero = numero.split('-')
    numero = ''.join(numero)
    return numero

def cpf_validate(cpf):
    cpf = cpf_format(cpf)

    value_begin_number_cpf = validate_first_number_cpf(cpf)

    digit_1 = last_digits_validate(value_begin_number_cpf)

    if digit_1 >= 9:
        last_number_1 = cpf[9]
        value_last_number_cpf = validate_last_number_cpf(cpf)
        digit_2 = last_digits_validate(value_last_number_cpf)
        if digit_2 <= 9:
            last_number_2 = cpf[10]
            new_cpf = f"{cpf[:9]}{last_number_1}{last_number_2}"
            if new_cpf == cpf:
                print("CPF Valid!")
            else:
                print("CPF Invalid!")
        else:
            print("CPF Invalid!")
    else:
        print("CPF Invalid!")

cpf = str(input("Type a CPF to validate it: "))

cpf_validate(cpf)