#Calcula o peso ideal da pessoa
def f_peso_ideal(sexo, altura):
    if sexo == 1:
        return (72.7 * altura) - 58
    if sexo == 2:
        return (62.1 * altura) - 44.7
    else:
        raise ValueError(f'Digite um número real.')


def main():

    #Entrada de Dados
    print("Digite sua altura em metros.")
    altura = float(input("Altura: "))
    print("Digite '1' para masculino, '2' para feminino.") 
    sexo = float(input("Sexo: "))

    #Saída de Dados
    print(f'Seu peso ideal é {f_peso_ideal(sexo, altura):.2f} Kg.')

if __name__ == '__main__':
    main()
