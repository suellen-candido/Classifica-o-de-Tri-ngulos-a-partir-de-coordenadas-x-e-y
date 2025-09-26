# Sugerir as coordenadas dos 3 pontos que formam o tipo de triângulo escolhido pelo usuário
escolha = int(input("Escola o tipo de triângulo\n[1] Equilátero\n[2] Isósceles\n[3] Escaleno\n[4] Sair\nR-> "))

if escolha == 1:
    # Equilátero -> todos os lados iguais
    P1 = (0, 0)
    P2 = (2, 0)
    P3 = (1, 1.73205)
    print(f"Coordenadas sugeridas:\nP1 = {P1}\nP2 = {P2}\nP3 = {P3}")
elif escolha == 2:
    # Isósceles -> dois lados iguais
    P1 = (0, 0)
    P2 = (4, 0)
    P3 = (2, 3)
    print(f"Coordenadas sugeridas:\nP1 = {P1}\nP2 = {P2}\nP3 = {P3}")
elif escolha == 3:
    # Escaleno -> Todos os lados são diferentes
    P1 = (0, 0)
    P2 = (4, 0)
    P3 = (3, 2)
    print(f"Coordenadas sugeridas:\nP1 = {P1}\nP2 = {P2}\nP3 = {P3}")
elif escolha == 4:
    print('Essa opção não existe')