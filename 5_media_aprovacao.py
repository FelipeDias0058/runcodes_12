#Determina o resultado final (nota, aprovação)
def f_resultado(a, b, c, d):

    #Calcula a média
    def f_media_final(a, b, c, d):
        return (a + (b * 2) + (c * 3) + d) / 7

    m_final = f_media_final(a, b, c, d)
    print(f'Média Final: {m_final:.2f}')

    try:
        if m_final >= 9.0:
            print("A")
        elif 7.5 <= m_final < 9.0:
            print("B")
        elif 6.0 <= m_final < 7.5:
            print("C")
        elif 4.0 <= m_final < 6.0:
            print("D")
        elif m_final < 4.0:
            print("E")
    finally:
        if 6.0 <= m_final:
            return "Aprovado"
        elif 6.0 >= m_final:
            return "Reprovado"
                

def main():

    #Entrada de Dados
    matricula = input("Digite sua matrícula: ")
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    n3 = float(input("Digite sua terceira nota: "))
    media_exercicios = float(input("Digite a média de seus exercícios: "))

    #Saída de Dados
    print('\n')
    print(matricula)
    print(f_resultado(n1, n2, n3, media_exercicios))


if __name__ == '__main__':
    main()
