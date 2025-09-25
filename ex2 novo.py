# Coordenadas vão ser armazenadas nas listas A, B e C
A = []
B = []
C = []

    # Registrando as coordenadas e armazenando elas em suas respectivas listas
    for i in range(3):
        print('-'*15)
        x = float(input(f"Digite X{i+1}: "))
        y = float(input(f"Digite Y{i+1}: "))

        if i == 0:  # Se o contador é igual a 0, os x1 e y1 vão para A
            A = [x, y]
        elif i == 1:  # Se o contador é igual a 1, os x2 e y2 vão para B
            B = [x, y]
        else:  # Se o contador é igual a 2, os x3 e y3 vão para C
            C = [x, y]

    print('-='*15)
    print(f"Coordenadas A:{A}\nCoordenadas B:{B}\nCoordenadas C:{C}")
    print('-='*15)

    # Vamos definir os lados com pitágoras
    l1 = ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5  # AB
    l2 = ((C[0]-A[0])**2 + (C[1]-A[1])**2)**0.5  # AC
    l3 = ((C[0]-B[0])**2 + (C[1]-B[1])**2)**0.5  # BC

    print('-='*15)

    # Tolerância para comparar floats
    tol = 1e-6

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