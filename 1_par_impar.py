
#Adiciona 5 ou 8 se o número
#for par ou ímpar.
def f_soma(n):
    if n % 2 == 0:
        return n + 5
    if n % 2 != 0:
        return n + 8
    else:
        raise ValueError(f'Digite um número inteiro.')

def main():

    #Entrada de Dados
    n = input("Digite um número: ")

    #Saída de Dados
    print(f_soma(int(n)))

if __name__ == '__main__':
    main()



    
