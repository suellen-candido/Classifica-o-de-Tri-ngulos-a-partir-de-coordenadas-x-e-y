# Coordenadas vão ser armazenadas nas listas A, B, C, D
A = []
B = []
C = []
D = []

escolha = int(input('O que você quer verificar?\n[1] Tipos de Triângulos\n[2] Tipos de Quadriláteros\n[3] Sair\nR->: '))
if escolha == 1:
    # Registrando as coordenadas e armazenando elas em suas respectivas listas
    for i in range(3):
        print('-'*15)
        x = float(input(f"Digite X{i+1}: "))
        y = float(input(f"Digite Y{i+1}: "))

        if i == 0:
            A = [x, y]
        elif i == 1:
            B = [x, y]
        else:
            C = [x, y]

    print('-='*15)
    print(f"Coordenadas A:{A}\nCoordenadas B:{B}\nCoordenadas C:{C}")
    print('-='*15)

    # Vamos definir os lados com pitágoras
    l1 = ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5  # AB
    l2 = ((C[0]-A[0])**2 + (C[1]-A[1])**2)**0.5  # AC
    l3 = ((C[0]-B[0])**2 + (C[1]-B[1])**2)**0.5  # BC

    print(f"Lado AB: {l1:.3}\nLado AC: {l2:.3}\nLado BC: {l3:.3}")
    print('-='*15)

    # Tolerância para comparar floats (aumentada para lidar com aproximações tipo 1.732)
    tol = 1e-2

    # Calculando área para descartar pontos colineares
    area = abs(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1])) / 2

    if area < tol:
        print("Não é um triângulo (os pontos são colineares).")
    elif abs(l1 - l2) < tol and abs(l1 - l3) < tol:
        print('É um triângulo: Equilátero.')
    elif abs(l1 - l2) < tol or abs(l1 - l3) < tol or abs(l2 - l3) < tol:
        print('É um triângulo: Isósceles.')
    else:
        print('É um triângulo: Escaleno.')

elif escolha == 2:
    # Registrando as coordenadas e armazenando elas em suas respectivas listas
    for i in range(4):
        print('-' * 15)
        x = float(input(f"Digite X{i + 1}: "))
        y = float(input(f"Digite Y{i + 1}: "))

        if i == 0:
            A = [x, y]
        elif i == 1:
            B = [x, y]
        elif i == 2:
            C = [x, y]
        else:
            D = [x, y]

    print('-=' * 15)
    print(f"Coordenadas A:{A}\nCoordenadas B:{B}\nCoordenadas C:{C}\nCoordenadas D:{D}")

    # Lados do quadrilátero
    l1 = ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5 # AB
    l2 = ((C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2) ** 0.5 # BC
    l3 = ((D[0] - C[0]) ** 2 + (D[1] - C[1]) ** 2) ** 0.5 # CD
    l4 = ((A[0] - D[0]) ** 2 + (A[1] - D[1]) ** 2) ** 0.5 # DA
    print('-=' * 15)

    print(f"Lado AB: {l1:.3f}\nLado BC: {l2:.3f}\nLado CD: {l3:.3f}\nLado DA: {l4:.3f}")

    # Diagonais
    print('-=' * 15)
    AC = ((C[0] - A[0])**2 + (C[1] - A[1])**2) ** 0.5
    BD = ((D[0] - B[0])**2 + (D[1] - B[1])**2) ** 0.5

    print(f"Diagonal AC: {AC:.3f}\nDiagonal BD: {BD:.3f}")

    # Produtos escalares para ângulos
    angulo1 = (B[0]-A[0])*(C[0]-B[0]) + (B[1]-A[1])*(C[1]-B[1])  # Ângulo em B
    angulo2 = (C[0]-B[0])*(D[0]-C[0]) + (C[1]-B[1])*(D[1]-C[1])  # Ângulo em C
    angulo3 = (D[0]-C[0])*(A[0]-D[0]) + (D[1]-C[1])*(A[1]-D[1])  # Ângulo em D
    angulo4 = (A[0]-D[0])*(B[0]-A[0]) + (A[1]-D[1])*(B[1]-A[1])  # Ângulo em A
    print('-=' * 15)

    print(f"Diagonal do Ângulo 1 (A): {angulo1}")
    print(f"Diagonal do Ângulo 2 (B): {angulo2}")
    print(f"Diagonal do Ângulo 3 (C): {angulo3}")
    print(f"Diagonal do Ângulo 4 (D): {angulo4}")
    print('-=' * 15)

    if abs(angulo1) < 1e-6 and abs(angulo2) < 1e-6 and abs(angulo3) < 1e-6 and abs(angulo4) < 1e-6:
        if abs(l1 - l2) < 1e-6 and abs(l2 - l3) < 1e-6 and abs(l3 - l4) < 1e-6:
            print("Esse quadrilátero é um: Quadrado")
        else:
            print("Esse quadrilátero é um: Retângulo")
    else:
        if abs(l1 - l3) < 1e-6 and abs(l2 - l4) < 1e-6:
            print("Esse quadrilátero é um: Paralelogramo")
        elif abs(l1 - l3) < 1e-6 or abs(l2 - l4) < 1e-6:
            print("Esse quadrilátero é um: Trapézio")
        else:
            print("Esse quadrilátero é um: Quadrilátero que não foi definido suas características")

elif escolha == 3:
    print('Saindo...')

else:
    print('Opção inválida')
