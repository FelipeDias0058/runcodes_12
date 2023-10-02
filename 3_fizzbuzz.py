
#Retorna 'FIZZ', 'BUZZ' ou 'FIZZBUZZ',
#dependendo dos parâmetros especificados. 
def f_fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    elif n % 3 == 0:
        return "FIZZ"
    elif n % 5 == 0:
        return "BUZZ"
    else:
        return n

def main():

    #Entrada de Dados
    n = input("")

    #Saída de Dados
    print(f_fizzbuzz(int(n)))

if __name__ == '__main__':
    main()



    
