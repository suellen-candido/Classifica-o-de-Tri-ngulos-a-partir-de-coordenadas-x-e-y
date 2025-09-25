# Ler um número inteiro de 5 dígitos e indicar se ele é palíndromo
print('-='*15)
print('Olá, seja bem-vindo(a)\nVamos ver se o valor é palíndromo.')
print('-='*15)

#Entrada do número
numero = int(input('Digite um número de 5 dígitos: '))

# Verificar se o número realmente tem 5 dígitos
quantidade_digitos = len(str(numero))

if quantidade_digitos == 5:
    # Verificar se ele é palíndromo
    if str(numero) == str(numero)[::-1]:  # inverte a string direto
        print(f'O valor {numero} é um palíndromo!')
    else:
        print(f'O valor {numero} não é um palíndromo.')

elif quantidade_digitos > 5:
    print('O número que você digitou tem mais de 5 dígitos. Tente novamente.')
else:
    print('O número que você digitou tem menos de 5 dígitos. Tente novamente')
