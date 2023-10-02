#Obtém a soma dos dígitos de um número inteiro.
def f_calc_digitos(n):

    #Função que calcula a soma dos dígitos de 'n'.
    def f_soma(n):
        sum = 0
        for digit in str(n): 
          sum += int(digit)      
        return sum

    #Condicional para a execução da função 'f_soma'.
    if 0 <= int(n) < 100000:
        return f_soma(n)
    else:
        return -1


def main():

    #Entrada de Dados
    n = input("Digite um número inteiro: ").strip()

    #Saída de Dados
    print(f'A soma dos dígitos é {f_calc_digitos(int(n))}.')


if __name__ == '__main__':
    main()
